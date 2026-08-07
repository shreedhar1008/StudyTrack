"""
StudyTrack — Recommendation Engine
Assigns a student to a behavioral cluster, compares them against top-20% 
performers in that cluster, and generates prioritized, weighted recommendations.
"""
import numpy as np
import pandas as pd
import joblib
import json

# --- Load artifacts once at import time ---
_cluster_model = joblib.load('models/student_cluster_model.pkl')
_cluster_scaler = joblib.load('models/cluster_scaler.pkl')

with open('models/cluster_names.json') as f:
    _cluster_names = json.load(f)

_benchmarks_df = pd.read_json('models/cluster_benchmarks.json', orient='index')

_CLUSTER_FEATURES = ['study_hours_per_day', 'social_media_hours', 'netflix_hours',
                      'sleep_hours', 'screen_time', 'exercise_frequency',
                      'motivation_level', 'stress_level', 'exam_anxiety_score',
                      'time_management_score']

_HABIT_COLS = _CLUSTER_FEATURES + ['attendance_percentage']

_IMPORTANCE_WEIGHTS = {
    'study_hours_per_day': 0.133, 'stress_level': 0.079, 'sleep_hours': 0.070,
    'attendance_percentage': 0.069, 'motivation_level': 0.062, 'time_management_score': 0.060,
    'screen_time': 0.052, 'netflix_hours': 0.049, 'social_media_hours': 0.048,
    'exam_anxiety_score': 0.040, 'exercise_frequency': 0.036
}

# Minimum gap size to be considered meaningful (not just statistical noise).
# Values are on each feature's natural scale (e.g., stress_level is 1-10).
_MIN_MEANINGFUL_GAP = {
    'study_hours_per_day': 0.5,      # half an hour or more
    'stress_level': 1.0,             # 1+ point on a 10-point scale
    'sleep_hours': 0.5,
    'attendance_percentage': 5.0,    # 5+ percentage points
    'motivation_level': 1.0,
    'time_management_score': 1.0,
    'screen_time': 1.0,
    'netflix_hours': 0.5,
    'social_media_hours': 0.5,
    'exam_anxiety_score': 1.0,
    'exercise_frequency': 1.0
}

_TEMPLATES = {
    'study_hours_per_day': {'label': 'Study Time',
        'text': "You're studying about {gap:.1f} fewer hours per day than top performers in your peer group. Even a modest increase — say, one focused 45-minute block — tends to compound over a semester."},
    'stress_level': {'label': 'Stress Management',
        'text': "Your stress level is running noticeably higher than students with similar habits who perform well. High stress doesn't just feel bad — it directly eats into focus and retention."},
    'sleep_hours': {'label': 'Sleep',
        'text': "You're getting about {gap:.1f} fewer hours of sleep than your top-performing peers. Sleep is when memory consolidation happens — skimping on it undercuts the studying you're already doing."},
    'attendance_percentage': {'label': 'Attendance',
        'text': "Your attendance is about {gap:.0f} percentage points below top performers in your group. Consistent attendance compounds — missed context is hard to fully recover from self-study alone."},
    'motivation_level': {'label': 'Motivation',
        'text': "Your motivation levels are lower than peers who are performing well with similar study patterns. This is often the real lever — habits are easier to sustain once motivation is addressed."},
    'time_management_score': {'label': 'Time Management',
        'text': "Your time management score suggests there's room to structure your study sessions more effectively — not necessarily study more, but study smarter."},
    'screen_time': {'label': 'Screen Time',
        'text': "Your overall screen time is higher than your top-performing peers by about {gap:.1f} hours. Worth auditing where that time actually goes."},
    'social_media_hours': {'label': 'Social Media',
        'text': "Social media usage is running higher than your peers who perform well — this is often one of the easiest, fastest wins since it's a direct time trade-off with study hours."},
    'netflix_hours': {'label': 'Entertainment Time',
        'text': "Entertainment/streaming time is above what your top-performing peers report — not a problem in moderation, but worth capping if study hours are tight."},
    'exam_anxiety_score': {'label': 'Exam Anxiety',
        'text': "Your exam anxiety is measurably higher than peers with strong outcomes. This often responds well to practice-testing and structured prep, not just 'staying calm.'"},
    'exercise_frequency': {'label': 'Exercise',
        'text': "You're exercising less frequently than your top-performing peers. Physical activity has a real, measurable link to focus and stress regulation — even light, regular movement helps."}
}


def assign_cluster(student_habits: dict) -> int:
    input_df = pd.DataFrame([[student_habits[f] for f in _CLUSTER_FEATURES]], columns=_CLUSTER_FEATURES)
    scaled_input = _cluster_scaler.transform(input_df)
    return int(_cluster_model.predict(scaled_input)[0])


def compute_gaps(student_habits: dict, cluster_id: int) -> dict:
    cluster_label = _cluster_names[str(cluster_id)]
    benchmark = _benchmarks_df.loc[cluster_label]

    gaps = {}
    for col in _HABIT_COLS:
        student_val = student_habits.get(col, benchmark[col])
        benchmark_val = benchmark[col]
        if col in ['stress_level', 'exam_anxiety_score']:
            gap = student_val - benchmark_val
        else:
            gap = benchmark_val - student_val
        gaps[col] = round(float(gap), 2)
    return gaps


def generate_recommendations(gaps: dict, top_n: int = 4) -> list:
    scored_gaps = []
    for habit, gap in gaps.items():
        min_threshold = _MIN_MEANINGFUL_GAP.get(habit, 0.3)
        if gap > min_threshold:  # only flag genuinely meaningful gaps now
            weight = _IMPORTANCE_WEIGHTS.get(habit, 0.03)
            scored_gaps.append((habit, gap, gap * weight))

    scored_gaps.sort(key=lambda x: x[2], reverse=True)

    recommendations = []
    for habit, gap, score in scored_gaps[:top_n]:
        template = _TEMPLATES[habit]
        recommendations.append({
            'area': template['label'],
            'priority_score': round(score, 3),
            'gap': gap,
            'recommendation': template['text'].format(gap=gap)
        })
    return recommendations


def get_full_recommendation(student_habits: dict, top_n: int = 4) -> dict:
    cluster_id = assign_cluster(student_habits)
    cluster_label = _cluster_names[str(cluster_id)]
    gaps = compute_gaps(student_habits, cluster_id)
    recommendations = generate_recommendations(gaps, top_n=top_n)

    return {
        'cluster': cluster_label,
        'gaps': gaps,
        'recommendations': recommendations,
        'is_strong_performer': len(recommendations) == 0
    }