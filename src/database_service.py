"""
StudyTrack — Database Service
Handles saving and retrieving student submissions from Supabase.
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

_supabase_url = os.environ.get("SUPABASE_URL")
_supabase_key = os.environ.get("SUPABASE_KEY")

_client: Client = create_client(_supabase_url, _supabase_key)


def save_submission(student_habits: dict, analysis: dict, risk: dict) -> dict:
    """
    Saves a student's submission and full results to the database.
    Returns the inserted row, or None if the save fails (non-blocking —
    the app should still work even if the database is temporarily down).
    """
    try:
        row = {
            "major": student_habits.get("major", "not specified"),
            "study_hours_per_day": student_habits.get("study_hours_per_day"),
            "social_media_hours": student_habits.get("social_media_hours"),
            "netflix_hours": student_habits.get("netflix_hours"),
            "sleep_hours": student_habits.get("sleep_hours"),
            "screen_time": student_habits.get("screen_time"),
            "exercise_frequency": student_habits.get("exercise_frequency"),
            "motivation_level": student_habits.get("motivation_level"),
            "stress_level": student_habits.get("stress_level"),
            "exam_anxiety_score": student_habits.get("exam_anxiety_score"),
            "time_management_score": student_habits.get("time_management_score"),
            "attendance_percentage": student_habits.get("attendance_percentage"),
            "cluster": analysis.get("cluster"),
            "is_strong_performer": analysis.get("is_strong_performer"),
            "recommendations": analysis.get("recommendations"),
            "personalized_message": analysis.get("personalized_message"),
            "risk_level": risk.get("risk_level"),
            "risk_factors": risk.get("risk_factors"),
        }
        result = _client.table("student_submissions").insert(row).execute()
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"Database save failed (non-blocking): {e}")
        return None


def get_recent_submissions(limit: int = 10) -> list:
    """Retrieves the most recent submissions (for a future history/admin view)."""
    try:
        result = (
            _client.table("student_submissions")
            .select("*")
            .order("created_at", desc=True)
            .limit(limit)
            .execute()
        )
        return result.data
    except Exception as e:
        print(f"Database fetch failed: {e}")
        return []