"""
StudyTrack — Transparent Risk Assessment Module
Flags students using explainable, threshold-based risk factors
rather than a black-box model (avoids reproducing dataset's synthetic dropout label).
"""

def calculate_risk_factors(student: dict) -> list:
    """Returns list of human-readable risk factor strings for a student profile."""
    factors = []
    if student.get('stress_level', 0) >= 8:
        factors.append('High stress level')
    if student.get('exam_anxiety_score', 0) >= 8:
        factors.append('High exam anxiety')
    if student.get('motivation_level', 10) <= 4:
        factors.append('Low motivation')
    if student.get('attendance_percentage', 100) < 75:
        factors.append('Low attendance')
    if student.get('mental_health_rating', 10) <= 4:
        factors.append('Low mental health rating')
    if student.get('sleep_hours', 8) < 6:
        factors.append('Insufficient sleep')
    return factors


def assign_risk_level(factor_count: int) -> str:
    """Maps risk factor count to a risk level label."""
    if factor_count <= 1:
        return 'Low'
    elif factor_count <= 3:
        return 'Moderate'
    else:
        return 'High'


def assess_student_risk(student: dict) -> dict:
    """Full risk assessment for a single student input dict."""
    factors = calculate_risk_factors(student)
    level = assign_risk_level(len(factors))
    return {
        'risk_level': level,
        'risk_factor_count': len(factors),
        'risk_factors': factors
    }