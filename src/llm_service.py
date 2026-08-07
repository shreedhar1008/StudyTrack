"""
StudyTrack — LLM Integration Service
Takes structured recommendation data (facts, already computed) and asks the LLM
to rewrite it into warm, natural, personalized language. The LLM never invents
numbers or facts — it only rephrases what we've already calculated.
"""
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
_MODEL = "llama-3.3-70b-versatile"

def _build_prompt(cluster: str, recommendations: list, student_context: dict) -> str:
    if not recommendations:
        return f"""You are StudyTrack, a supportive AI study coach writing directly to a student.

Student's behavioral profile: {cluster}
Student's major: {student_context.get('major', 'not specified')}

This student's habits are already strong — they don't have any significant gaps compared to top-performing peers in their group. Write a short (100-150 word), warm, genuine congratulatory message that:
1. Acknowledges their strong habits specifically (mention their profile type naturally, in plain words, not as a label)
2. Encourages them to maintain consistency rather than implying they need to change anything
3. Suggests one forward-looking idea they could explore on their own (e.g., trying a slightly harder personal goal, helping a peer who's struggling, deepening focus in one subject) — NOT a meeting, appointment, or anything requiring another person's availability
4. Does NOT invent any weaknesses or problems that don't exist
5. Does NOT suggest scheduling a meeting, call, or appointment of any kind — you are a self-serve app, not a human advisor

Write only the message, no preamble."""

    rec_lines = "\n".join(
        [f"- {r['area']}: {r['recommendation']}" for r in recommendations]
    )

    prompt = f"""You are StudyTrack, a supportive AI study coach writing directly to a student.

Student's behavioral profile: {cluster}
Student's major: {student_context.get('major', 'not specified')}

Here are data-backed recommendations already calculated for this student (based on comparing them to top-performing peers with similar habits). Do NOT invent any new numbers, statistics, or facts. Your job is ONLY to rewrite these into a warm, natural, encouraging message — as if a caring coach is speaking directly to the student, not listing bullet points robotically.

Recommendations (facts, do not alter numbers):
{rec_lines}

Write a short, personalized message (150-200 words) that:
1. Opens with genuine encouragement, referencing their specific situation naturally
2. Weaves the recommendations into flowing, conversational advice — not a bullet list
3. Ends with ONE concrete next step the student can take on their own TODAY (e.g., "start tonight by...", "tomorrow morning, try...") — never suggest scheduling a meeting, call, or appointment with anyone
4. Sounds like a real person who cares, not corporate or robotic
5. Does NOT invent any statistics not given above

Write only the message, no preamble."""
    return prompt


def generate_personalized_message(cluster: str, recommendations: list, student_context: dict = None) -> str:
    """
    Calls Groq LLM to turn structured recommendations into a natural,
    personalized message. Falls back to templated text if the API fails.
    """
    student_context = student_context or {}
    prompt = _build_prompt(cluster, recommendations, student_context)

    try:
        response = _client.chat.completions.create(
            model=_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=400,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Fallback: if API fails (rate limit, network issue), don't crash — 
        # return the templated recommendations so the app still works
        fallback = "Here's what we found based on your habits:\n\n"
        fallback += "\n".join([f"• {r['recommendation']}" for r in recommendations])
        return fallback

def generate_plan_summary(cluster: str, recommendations: list, target_study_hours: float, student_context: dict = None) -> str:
    """
    Generates a short, motivating intro paragraph for the student's weekly study plan.
    This does NOT generate the plan itself (that stays deterministic/rule-based) —
    only a personalized framing message shown above the plan.
    """
    student_context = student_context or {}
    focus_areas = ", ".join([r['area'] for r in recommendations]) if recommendations else "maintaining your strong habits"

    prompt = f"""You are StudyTrack, an AI study coach. Write a brief (60-90 word) introduction 
for a student's personalized weekly study plan.

Student's profile: {cluster}
Target daily study hours: {target_study_hours}
This week's focus areas: {focus_areas}

Write an intro that:
1. Briefly explains WHY the plan is structured this way (tie it to their focus areas)
2. Sounds encouraging and specific, not generic
3. Does NOT list out the daily schedule (that's shown separately below this text)
4. Does NOT suggest meetings or appointments

Write only the intro text, no preamble."""

    try:
        response = _client.chat.completions.create(
            model=_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return f"This week's plan focuses on {focus_areas}, with a target of {target_study_hours} hours of study per day, structured to fit sustainably into your routine."