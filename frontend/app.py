import streamlit as st
import requests

API_URL = "https://studytrack-backend-68aq.onrender.com"

st.set_page_config(page_title="StudyTrack", page_icon="📚", layout="centered")

st.title("📚 StudyTrack")
st.caption("AI-based personalized study habit recommendations")

st.markdown("Fill in your current habits below to get a personalized analysis, recommendations, and a 7-day study plan — based on real patterns from thousands of students.")

with st.form("student_form"):
    st.subheader("Study & Time")
    col1, col2 = st.columns(2)
    with col1:
        study_hours = st.number_input("Study hours per day", min_value=0.0, max_value=24.0, value=3.0, step=0.5)
        social_media_hours = st.number_input("Social media hours per day", min_value=0.0, max_value=24.0, value=2.0, step=0.5)
        netflix_hours = st.number_input("Netflix/streaming hours per day", min_value=0.0, max_value=24.0, value=1.0, step=0.5)
        screen_time = st.number_input("Total screen time per day (hrs)", min_value=0.0, max_value=24.0, value=8.0, step=0.5)
    with col2:
        sleep_hours = st.number_input("Sleep hours per night", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
        exercise_frequency = st.number_input("Exercise sessions per week", min_value=0.0, max_value=14.0, value=2.0, step=1.0)
        attendance_percentage = st.slider("Class attendance (%)", min_value=0, max_value=100, value=80)

    st.subheader("Wellbeing & Mindset")
    col3, col4 = st.columns(2)
    with col3:
        motivation_level = st.slider("Motivation level (1-10)", min_value=1, max_value=10, value=5)
        stress_level = st.slider("Stress level (1-10)", min_value=1, max_value=10, value=5)
    with col4:
        exam_anxiety_score = st.slider("Exam anxiety (1-10)", min_value=1, max_value=10, value=5)
        time_management_score = st.slider("Time management skill (1-10)", min_value=1, max_value=10, value=5)

    major = st.text_input("Your major/field of study (optional)", value="")

    submitted = st.form_submit_button("Get My Personalized Analysis", use_container_width=True)

if submitted:
    payload = {
        "study_hours_per_day": study_hours,
        "social_media_hours": social_media_hours,
        "netflix_hours": netflix_hours,
        "sleep_hours": sleep_hours,
        "screen_time": screen_time,
        "exercise_frequency": exercise_frequency,
        "motivation_level": motivation_level,
        "stress_level": stress_level,
        "exam_anxiety_score": exam_anxiety_score,
        "time_management_score": time_management_score,
        "attendance_percentage": attendance_percentage,
        "major": major if major else "not specified"
    }

    with st.spinner("Analyzing your habits and generating your personalized plan..."):
        try:
            analyze_resp = requests.post(f"{API_URL}/analyze", json=payload, timeout=30)
            plan_resp = requests.post(f"{API_URL}/plan", json=payload, timeout=30)

            if analyze_resp.status_code == 200 and plan_resp.status_code == 200:
                analysis = analyze_resp.json()
                plan = plan_resp.json()

                st.divider()

                # --- Cluster & Personalized Message ---
                st.subheader("Your Personalized Analysis")
                st.caption(f"Closest behavioral pattern match: *{analysis['cluster']}* (based on motivation, stress, and study habits — see specific gaps below)")
                if analysis["is_strong_performer"]:
                    st.success(analysis["personalized_message"])
                else:
                    st.info(analysis["personalized_message"])

                # --- Recommendations ---
                if analysis["recommendations"]:
                    st.subheader("🎯 Priority Recommendations")
                    for i, rec in enumerate(analysis["recommendations"], 1):
                        with st.expander(f"{i}. {rec['area']}", expanded=(i == 1)):
                            st.write(rec["recommendation"])

                # --- Study Plan ---
                st.divider()
                st.subheader("📅 Your 7-Day Study Plan")
                st.caption(plan["plan_summary"])
                st.metric("Target study hours/day", f"{plan['target_study_hours_per_day']}h",
                          delta=f"+{round(plan['target_study_hours_per_day'] - plan['current_study_hours_per_day'], 1)}h from current")

                days = list(plan["weekly_plan"].keys())
                tabs = st.tabs(days)
                for tab, day in zip(tabs, days):
                    with tab:
                        for block in plan["weekly_plan"][day]:
                            st.markdown(f"**{block['time']}:** {block['activity']}")

            else:
                st.error(f"Something went wrong. Analyze status: {analyze_resp.status_code}, Plan status: {plan_resp.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend API. Make sure the FastAPI server is running (`uvicorn backend.main:app --reload`).")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")