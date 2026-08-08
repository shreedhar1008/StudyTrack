from pydantic import BaseModel, Field
from typing import Optional


class StudentInput(BaseModel):
    """All the habit/lifestyle inputs we need from the student."""
    study_hours_per_day: float = Field(..., ge=0, le=24)
    social_media_hours: float = Field(..., ge=0, le=24)
    netflix_hours: float = Field(..., ge=0, le=24)
    sleep_hours: float = Field(..., ge=0, le=24)
    screen_time: float = Field(..., ge=0, le=24)
    exercise_frequency: float = Field(..., ge=0)
    motivation_level: float = Field(..., ge=1, le=10)
    stress_level: float = Field(..., ge=1, le=10)
    exam_anxiety_score: float = Field(..., ge=1, le=10)
    time_management_score: float = Field(..., ge=1, le=10)
    attendance_percentage: float = Field(..., ge=0, le=100)
    major: Optional[str] = "not specified"


class RecommendationItem(BaseModel):
    area: str
    priority_score: float
    gap: float
    recommendation: str


class AnalysisResponse(BaseModel):
    cluster: str
    is_strong_performer: bool
    recommendations: list[RecommendationItem]
    personalized_message: str


class StudyPlanResponse(BaseModel):
    target_study_hours_per_day: float
    current_study_hours_per_day: float
    plan_summary: str
    weekly_plan: dict