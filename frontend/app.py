import streamlit as st
import requests

API_URL = "https://studytrack-backend-68aq.onrender.com"  # live Render backend

st.set_page_config(page_title="StudyTrack", page_icon="📚", layout="centered")

# ============================================================
# DESIGN SYSTEM — dark navy + mint/amber/coral accents
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg: #F5F6FA;
    --card: rgba(20, 27, 45, 0.75);
    --card-solid: #141B2D;
    --card-border: rgba(255,255,255,0.1);
    --card-shadow: 0 2px 8px rgba(0,0,0,0.1), 0 8px 24px rgba(0,0,0,0.06);
    --card-shadow-hover: 0 4px 14px rgba(0,0,0,0.15), 0 12px 32px rgba(0,0,0,0.1);
    --emerald: #34D399;
    --emerald-light: rgba(52,211,153,0.1);
    --amber: #F5A623;
    --amber-light: rgba(245,166,35,0.12);
    --rose: #FB7185;
    --rose-light: rgba(251,113,133,0.1);
    --indigo: #4F46E5;
    --page-text: #1A1D2E;
    --page-muted: #6B7280;
    --card-text: #E8EDF5;
    --card-muted: #8B94A8;
}

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: var(--bg) !important;
    color: var(--page-text);
}

/* Force Streamlit's inner containers */
.stApp > header { background: transparent !important; }
div[data-testid="stAppViewBlockContainer"] { color: var(--page-text); }

#MainMenu, footer, header[data-testid="stHeader"] {
    visibility: hidden;
}

/* ---- Eyebrow / pill tags ---- */
.eyebrow {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    color: var(--emerald);
    background: rgba(52,211,153,0.08);
    border: 1px solid rgba(52,211,153,0.2);
    border-radius: 999px;
    padding: 0.3rem 0.9rem;
    margin-bottom: 0.6rem;
}

/* ---- Headings (dark text on light bg) ---- */
h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--page-text) !important;
    -webkit-text-fill-color: var(--page-text) !important;
}
h2, h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    color: var(--page-text) !important;
}
.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--emerald);
    margin: 1.6rem 0 0.6rem 0;
    font-weight: 600;
}
.section-label.amber { color: var(--amber); }

/* ---- Stat-style number inputs — DARK cards ---- */
div[data-testid="stNumberInput"] {
    background: var(--card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 0.7rem 1rem 0.4rem 1rem;
    box-shadow: var(--card-shadow);
    transition: box-shadow 0.25s ease, transform 0.2s ease;
}
div[data-testid="stNumberInput"]:hover {
    box-shadow: var(--card-shadow-hover);
    transform: translateY(-1px);
}
div[data-testid="stNumberInput"] label p {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--card-muted) !important;
}
div[data-testid="stNumberInput"] input {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.6rem !important;
    font-weight: 600 !important;
    color: var(--emerald) !important;
    background: transparent !important;
}
div[data-testid="stNumberInput"] button {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 50% !important;
    color: var(--card-text) !important;
    border: 1px solid var(--card-border) !important;
}
div[data-testid="stNumberInput"] button:hover {
    background: var(--emerald-light) !important;
    color: var(--emerald) !important;
    border-color: rgba(52,211,153,0.3) !important;
}

/* ---- Sliders — DARK cards ---- */
div[data-testid="stSlider"] {
    background: var(--card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 0.9rem 1.2rem 1.1rem 1.2rem;
    box-shadow: var(--card-shadow);
    transition: box-shadow 0.25s ease, transform 0.2s ease;
}
div[data-testid="stSlider"]:hover {
    box-shadow: var(--card-shadow-hover);
    transform: translateY(-1px);
}
div[data-testid="stSlider"] label p {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--card-muted) !important;
}
div[data-testid="stSlider"] [role="slider"] {
    background-color: var(--emerald) !important;
    border: 3px solid var(--card) !important;
    box-shadow: 0 0 0 2px var(--emerald), 0 2px 6px rgba(52,211,153,0.3) !important;
}
div[data-testid="stSlider"] div[data-baseweb="slider"] > div > div {
    background: var(--emerald) !important;
}
div[data-testid="stSlider"] div[data-baseweb="slider"] > div:first-child {
    background: #263048 !important;
}

/* ---- Text input ---- */
div[data-testid="stTextInput"] input {
    background: var(--card) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: 14px !important;
    color: var(--card-text) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    box-shadow: var(--card-shadow) !important;
    transition: box-shadow 0.2s ease !important;
}
div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 3px rgba(52,211,153,0.15), var(--card-shadow) !important;
}
div[data-testid="stTextInput"] label p {
    color: var(--page-muted) !important;
}

/* ---- Submit button ---- */
.stButton button, .stFormSubmitButton button {
    background: linear-gradient(135deg, #34D399, #2DBE8A) !important;
    color: #06251A !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 0.85rem 2rem !important;
    box-shadow: 0 4px 20px rgba(52,211,153,0.3), 0 1px 3px rgba(0,0,0,0.1);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.stButton button:hover, .stFormSubmitButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 28px rgba(52,211,153,0.45), 0 2px 6px rgba(0,0,0,0.12);
}

/* ---- Recommendation cards ---- */
.rec-card {
    background: var(--card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--card-border);
    border-left: 4px solid var(--accent, var(--emerald));
    border-radius: 14px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    box-shadow: var(--card-shadow);
    transition: box-shadow 0.25s ease, transform 0.2s ease;
}
.rec-card:hover {
    box-shadow: var(--card-shadow-hover);
    transform: translateY(-2px);
}
.rec-card .rec-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent, var(--emerald));
    font-weight: 600;
}
.rec-card .rec-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--card-text);
    margin: 0.15rem 0 0.4rem 0;
}
.rec-card .rec-body {
    color: var(--card-muted);
    font-size: 0.92rem;
    line-height: 1.55;
}

/* ---- Message panel ---- */
.msg-panel {
    background: rgba(52,211,153,0.06);
    border: 1px solid rgba(52,211,153,0.15);
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    color: var(--page-muted);
    line-height: 1.65;
    font-size: 0.98rem;
}

/* ---- Plan header metric card — DARK ---- */
.plan-metric {
    background: var(--card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--card-border);
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    box-shadow: var(--card-shadow);
}
.plan-metric .value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: var(--emerald);
}
.plan-metric .delta {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--emerald);
    background: var(--emerald-light);
    border-radius: 999px;
    padding: 0.2rem 0.7rem;
    margin-top: 0.4rem;
}

/* ---- Timeline blocks — DARK cards on light bg ---- */
.timeline-item {
    display: flex;
    gap: 0.9rem;
    align-items: flex-start;
    background: var(--card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem;
    box-shadow: var(--card-shadow);
    transition: box-shadow 0.25s ease, transform 0.2s ease;
}
.timeline-item:hover {
    box-shadow: var(--card-shadow-hover);
    transform: translateY(-2px);
}
.timeline-icon {
    font-size: 1.3rem;
    line-height: 1;
    background: rgba(52,211,153,0.1);
    border-radius: 10px;
    padding: 0.45rem;
    flex-shrink: 0;
}
.timeline-time {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--amber);
    font-weight: 600;
}
.timeline-activity {
    font-size: 0.95rem;
    color: var(--card-muted);
    margin-top: 0.15rem;
}

/* ---- Tabs styled as pills ---- */
button[data-baseweb="tab"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.78rem !important;
    color: var(--page-muted) !important;
    border-radius: 8px !important;
    transition: background 0.15s ease, color 0.15s ease !important;
}
button[data-baseweb="tab"]:hover {
    background: rgba(52,211,153,0.06) !important;
    color: var(--emerald) !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--emerald) !important;
    font-weight: 600 !important;
}
div[data-baseweb="tab-highlight"] {
    background-color: var(--emerald) !important;
}

/* ---- Form container — subtle frosted ---- */
div[data-testid="stForm"] {
    background: rgba(20, 27, 45, 0.04);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(0,0,0,0.06);
    border-radius: 20px;
    padding: 1.4rem 1.6rem;
}

hr {
    border-color: rgba(0,0,0,0.08) !important;
    opacity: 0.6;
}

/* ---- Spinner ---- */
.stSpinner > div {
    color: var(--emerald) !important;
}

/* ---- Description / subtitle text ---- */
.subtitle-text {
    color: var(--muted);
    margin-top: -0.6rem;
    line-height: 1.6;
}

/* ---- Risk badge ---- */
.risk-badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    padding: 0.25rem 0.8rem;
    border-radius: 999px;
    font-weight: 600;
}
.risk-badge.low { color: var(--emerald); background: var(--emerald-light); }
.risk-badge.medium { color: var(--amber); background: var(--amber-light); }
.risk-badge.high { color: var(--rose); background: var(--rose-light); }
</style>
""", unsafe_allow_html=True)

# ============================================================
# ICON MAP for study plan timeline
# ============================================================
ICON_MAP = {
    "morning": "🌤️",
    "afternoon": "📖",
    "evening": "🌙",
    "night": "😴",
    "before study block": "🧘",
    "mid-session": "⏱️",
}

def get_icon(time_label: str) -> str:
    return ICON_MAP.get(time_label.strip().lower(), "•")

# Recommendation area -> accent color
ACCENT_MAP = {
    "Attendance": "#F5A623",
    "Time Management": "#F5A623",
    "Stress Management": "#FB7185",
    "Exam Anxiety": "#FB7185",
    "Motivation": "#34D399",
    "Study Time": "#34D399",
    "Exercise": "#34D399",
    "Screen Time": "#FB7185",
    "Social Media": "#FB7185",
    "Entertainment Time": "#FB7185",
    "Sleep": "#34D399",
}

# ============================================================
# HEADER
# ============================================================
st.markdown('<span class="eyebrow">AI STUDY COACH</span>', unsafe_allow_html=True)
st.title("📚 StudyTrack")
st.markdown(
    '<p style="color:#6B7280; margin-top:-0.6rem;">Fill in your current habits to get a personalized analysis, '
    'recommendations, and a 7-day study plan — based on real patterns from thousands of students.</p>',
    unsafe_allow_html=True
)

# ============================================================
# FORM
# ============================================================
with st.form("student_form"):
    st.markdown('<div class="section-label">Study &amp; Time</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        study_hours = st.number_input("STUDY HOURS/DAY", min_value=0.0, max_value=24.0, value=3.0, step=0.5)
        social_media_hours = st.number_input("SOCIAL MEDIA HRS", min_value=0.0, max_value=24.0, value=2.0, step=0.5)
        netflix_hours = st.number_input("NETFLIX/STREAMING HRS", min_value=0.0, max_value=24.0, value=1.0, step=0.5)
    with col2:
        sleep_hours = st.number_input("SLEEP HOURS", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
        exercise_frequency = st.number_input("EXERCISE SESSIONS/WK", min_value=0.0, max_value=14.0, value=2.0, step=1.0)
        attendance_percentage = st.slider("CLASS ATTENDANCE (%)", min_value=0, max_value=100, value=80)

    col_screen, _ = st.columns([1, 1])
    with col_screen:
        screen_time = st.number_input("TOTAL SCREEN TIME", min_value=0.0, max_value=24.0, value=8.0, step=0.5)

    st.markdown('<div class="section-label amber">Wellbeing &amp; Mindset</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        motivation_level = st.slider("MOTIVATION", min_value=1, max_value=10, value=5)
        stress_level = st.slider("STRESS", min_value=1, max_value=10, value=5)
    with col4:
        exam_anxiety_score = st.slider("ANXIETY", min_value=1, max_value=10, value=5)
        time_management_score = st.slider("TIME MANAGEMENT", min_value=1, max_value=10, value=5)

    major = st.text_input("Your major/field of study (optional)", value="")

    submitted = st.form_submit_button("✨ Get My Personalized Analysis", use_container_width=True)

# ============================================================
# RESULTS
# ============================================================
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
            analyze_resp = requests.post(f"{API_URL}/analyze", json=payload, timeout=60)
            plan_resp = requests.post(f"{API_URL}/plan", json=payload, timeout=60)

            if analyze_resp.status_code == 200 and plan_resp.status_code == 200:
                analysis = analyze_resp.json()
                plan = plan_resp.json()

                st.markdown("---")

                # --- Personalized message panel ---
                st.markdown('<span class="eyebrow">PERSONALIZED ANALYSIS</span>', unsafe_allow_html=True)
                st.markdown(f"### Closest match: {analysis['cluster']}")
                st.markdown(f'<div class="msg-panel">{analysis["personalized_message"]}</div>', unsafe_allow_html=True)

                # --- Recommendations ---
                if analysis["recommendations"]:
                    st.markdown('<div class="section-label">Priority Recommendations</div>', unsafe_allow_html=True)
                    for rec in analysis["recommendations"]:
                        accent = ACCENT_MAP.get(rec["area"], "#34D399")
                        st.markdown(f"""
                        <div class="rec-card" style="--accent:{accent}">
                            <div class="rec-eyebrow">{rec['area']}</div>
                            <div class="rec-body">{rec['recommendation']}</div>
                        </div>
                        """, unsafe_allow_html=True)

                # --- Study Plan ---
                st.markdown("---")
                st.markdown('<span class="eyebrow">7-DAY PLAN</span>', unsafe_allow_html=True)
                st.markdown("### Your Study Plan")
                st.markdown(f'<p style="color:#6B7280;">{plan["plan_summary"]}</p>', unsafe_allow_html=True)

                delta = round(plan['target_study_hours_per_day'] - plan['current_study_hours_per_day'], 1)
                delta_str = f"+{delta}h from current" if delta >= 0 else f"{delta}h from current"
                st.markdown(f"""
                <div class="plan-metric">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:0.7rem; letter-spacing:0.08em; color:#8B94A8; text-transform:uppercase;">Target study hours/day</div>
                    <div class="value">{plan['target_study_hours_per_day']}h</div>
                    <div class="delta">{delta_str}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                days = list(plan["weekly_plan"].keys())
                tabs = st.tabs(days)
                for tab, day in zip(tabs, days):
                    with tab:
                        for block in plan["weekly_plan"][day]:
                            icon = get_icon(block["time"])
                            st.markdown(f"""
                            <div class="timeline-item">
                                <div class="timeline-icon">{icon}</div>
                                <div>
                                    <div class="timeline-time">{block['time']}</div>
                                    <div class="timeline-activity">{block['activity']}</div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

            else:
                st.error(f"Something went wrong. Analyze status: {analyze_resp.status_code}, Plan status: {plan_resp.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend API. Please try again in a moment (the free server may be waking up).")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")