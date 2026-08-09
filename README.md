# StudyTrack: AI-Based Student Study Habit Recommendation System

StudyTrack analyzes a student's study habits, lifestyle, and performance data to generate personalized, data-backed recommendations and a day-by-day study plan built on real patterns mined from an 80,000-student dataset, not generic advice.

##  Project Status: In Development

## Features (so far)
- Data-driven clustering of students into 5 behavioral profiles
- ML-based exam score prediction (Random Forest, R²=0.87)
- Transparent, explainable risk assessment (no black-box scoring)
- Personalized recommendation engine using peer-benchmark gap analysis
- Auto-generated day-by-day study plans

## Tech Stack
- **ML/Data:** Python, Pandas, Scikit-learn
- **LLM:** Groq API (free tier)
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Database:** Supabase (Postgres)
- **Deployment:** Render + Streamlit Cloud

## Project Structure
```text
studytrack/
├── data/       # Raw and cleaned datasets
├── models/     # Trained ML models and artifacts
├── notebooks/  # Analysis and model development notebooks
├── src/        # Reusable Python modules (recommendation engine, etc.)
├── backend/    # FastAPI backend (coming soon)
└── frontend/   # Streamlit frontend (coming soon)
```

## Author
Shreedhar Shiragur
