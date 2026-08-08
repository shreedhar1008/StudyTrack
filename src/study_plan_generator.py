"""
StudyTrack — Day-by-Day Study Plan Generator
Builds a personalized 7-day plan using the student's available time,
current habits, and their top recommendation areas.
"""

_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def _recommended_study_hours(current_hours: float, gap: float) -> float:
    """Nudge study hours up gradually, not a jarring jump — sustainable over a jarring one."""
    if gap <= 0:
        return round(current_hours, 1)
    increase = min(gap * 0.5, 1.5)  # cap daily increase to keep it realistic/sustainable
    return round(current_hours + increase, 1)


def generate_study_plan(student_habits: dict, recommendations: list) -> dict:
    current_study_hours = student_habits.get('study_hours_per_day', 2.0)
    current_sleep_hours = student_habits.get('sleep_hours', 7.0)

    study_gap = next((r['gap'] for r in recommendations if r['area'] == 'Study Time'), 0)
    target_study_hours = _recommended_study_hours(current_study_hours, study_gap)

    rec_areas = {r['area'] for r in recommendations}

    # Rotate which type of work gets emphasized each weekday, so the plan doesn't feel identical daily
    weekday_focus = {
        'Monday': ('New material / hardest subject', 'Practice problems'),
        'Tuesday': ('Review previous day + new material', 'Flashcards / active recall'),
        'Wednesday': ('New material / hardest subject', 'Group study or discussion-based review'),
        'Thursday': ('Practice problems / past papers', 'Review weak areas from this week'),
        'Friday': ('Lighter review + consolidation', 'Wrap up any pending coursework'),
    }

    plan = {}
    for i, day in enumerate(_DAYS):
        blocks = []
        is_weekend = day in ['Saturday', 'Sunday']

        if is_weekend:
            block1_label, block2_label = 'Weekly review of all subjects', 'Preview next week\'s material'
        else:
            block1_label, block2_label = weekday_focus[day]

        if target_study_hours <= 2:
            blocks.append({'time': 'Evening', 'activity': f'Focused study session ({target_study_hours}h) — {block1_label.lower()}'})
        else:
            first_block = round(target_study_hours * 0.6, 1)
            second_block = round(target_study_hours - first_block, 1)
            blocks.append({'time': 'Afternoon', 'activity': f'Study block 1 ({first_block}h) — {block1_label}'})
            blocks.append({'time': 'Evening', 'activity': f'Study block 2 ({second_block}h) — {block2_label}'})

        if 'Stress Management' in rec_areas:
            blocks.append({'time': 'Before study block', 'activity': '10-min breathing/walk break — lowers cortisol before you sit down to focus'})

        if 'Exam Anxiety' in rec_areas and not is_weekend:
            blocks.append({'time': 'Mid-session', 'activity': 'Timed practice questions (15-20 min) — builds exam-condition familiarity'})

        if 'Exercise' in rec_areas:
            blocks.append({'time': 'Morning', 'activity': '20-30 min light exercise — walk, stretch, or sport'})

        if 'Time Management' in rec_areas and day == 'Sunday':
            blocks.append({'time': 'Evening', 'activity': 'Weekly planning: review upcoming deadlines, block study time in calendar'})

        if 'Attendance' in rec_areas and not is_weekend:
            blocks.append({'time': 'Morning', 'activity': 'Attend all scheduled classes — missed classes compound faster than they feel like they do'})

        sleep_target = max(current_sleep_hours, 7.0)
        blocks.append({'time': 'Night', 'activity': f'Lights out by target time for {sleep_target}h sleep — protects memory consolidation from today\'s studying'})

        if is_weekend:
            blocks.append({'time': 'Afternoon', 'activity': 'Free time / hobby / social — recovery is part of a sustainable routine, not a cheat day'})

        plan[day] = blocks

    return {
        'target_study_hours_per_day': target_study_hours,
        'current_study_hours_per_day': current_study_hours,
        'weekly_plan': plan
    }