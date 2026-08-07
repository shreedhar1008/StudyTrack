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
        return f"""You are a supportive academic advisor writing to a student.

Student's behavioral profile: {cluster}
Student's major: {student_context.get('major', 'not specified')}

This student's habits are already strong — they don't have any significant gaps compared to top-performing peers in their group. Write a short (100-150 word), warm, genuine congratulatory message that:
1. Acknowledges their strong habits specifically (mention their profile type naturally)
2. Encourages them to maintain consistency rather than implying they need to change anything
3. Suggests one forward-looking idea (e.g., mentoring others, taking on a slightly harder goal) rather than a "fix"
4. Does NOT invent any weaknesses or problems that don't exist

Write only the message, no preamble."""

    rec_lines = "\n".join(
        [f"- {r['area']}: {r['recommendation']}" for r in recommendations]
    )
    # ... rest of the existing function unchanged

def _build_prompt(cluster: str, recommendations: list, student_context: dict) -> str:
    rec_lines = "\n".join(
        [f"- {r['area']}: {r['recommendation']}" for r in recommendations]
    )

    prompt = f"""You are a supportive, experienced academic advisor writing directly to a student.

Student's behavioral profile: {cluster}
Student's major: {student_context.get('major', 'not specified')}

Here are data-backed recommendations already calculated for this student (based on comparing them to top-performing peers with similar habits). Do NOT invent any new numbers, statistics, or facts. Your job is ONLY to rewrite these into a warm, natural, encouraging message — as if a caring advisor is speaking directly to the student, not listing bullet points robotically.

Recommendations (facts, do not alter numbers):
{rec_lines}

Write a short, personalized message (150-200 words) that:
1. Opens with genuine encouragement, referencing their specific profile type naturally (don't just say "profile type X")
2. Weaves the recommendations into flowing, conversational advice — not a bullet list
3. Ends with one motivating, concrete next step
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