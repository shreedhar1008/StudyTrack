from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import StudentInput, AnalysisResponse, StudyPlanResponse
from src.recommendation_engine import get_full_recommendation
from src.study_plan_generator import generate_study_plan
from src.llm_service import generate_personalized_message, generate_plan_summary
from src.risk_assessor import assess_student_risk
from src.database_service import save_submission
from src.database_service import get_recent_submissions
from src.database_service import get_submissions_by_anon_id

app = FastAPI(
    title="StudyTrack API",
    description="AI-based student study habit recommendation system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "StudyTrack API is running", "status": "healthy"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_student(student: StudentInput):
    try:
        habits = student.model_dump(exclude={"major"})
        habits["major"] = student.major
        habits["anon_id"] = student.anon_id

        result = get_full_recommendation(habits)

        message = generate_personalized_message(
            result["cluster"],
            result["recommendations"],
            {"major": student.major}
        )

        risk = assess_student_risk(habits)

        save_submission(habits, {**result, "personalized_message": message}, risk)

        return AnalysisResponse(
            cluster=result["cluster"],
            is_strong_performer=result["is_strong_performer"],
            recommendations=result["recommendations"],
            personalized_message=message
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.post("/plan", response_model=StudyPlanResponse)
def get_study_plan(student: StudentInput):
    """
    Generates a personalized 7-day study plan based on the student's habits.
    """
    try:
        habits = student.model_dump(exclude={"major"})
        result = get_full_recommendation(habits)
        plan = generate_study_plan(habits, result["recommendations"])

        summary = generate_plan_summary(
            result["cluster"],
            result["recommendations"],
            plan["target_study_hours_per_day"],
            {"major": student.major}
        )

        return StudyPlanResponse(
            target_study_hours_per_day=plan["target_study_hours_per_day"],
            current_study_hours_per_day=plan["current_study_hours_per_day"],
            plan_summary=summary,
            weekly_plan=plan["weekly_plan"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Plan generation failed: {str(e)}")


@app.post("/risk-check")
def check_risk(student: StudentInput):
    """
    Quick, transparent risk assessment — separate from the main analysis
    since it's meant to be a fast, lightweight early-warning check.
    """
    try:
        habits = student.model_dump(exclude={"major"})
        risk = assess_student_risk(habits)
        return risk
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Risk check failed: {str(e)}")

@app.get("/history/{anon_id}")
def get_history(anon_id: str):
    """Returns past submissions for a given anonymous user ID."""
    try:
        submissions = get_submissions_by_anon_id(anon_id)
        return {"count": len(submissions), "submissions": submissions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"History fetch failed: {str(e)}")