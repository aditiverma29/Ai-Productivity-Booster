import os
import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key
else:
    st.error("Google API Key is missing. Please set it in your .env file.")

# Agents Setup
routine_builder = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Creates structured productivity plans based on user-defined goals.",
    instructions=[
        "Generate a full-day routine with blocks for work, breaks, meals, and deep focus time.",
        "Prioritize user's major and minor goals across daily, weekly, and monthly context.",
        "Incorporate user’s productivity style (Pomodoro, Deep Work, Balanced).",
        "Use DuckDuckGo for trending techniques or calendar tips if needed."
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

focus_trainer = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Suggests methods and tools to reduce distractions and improve focus.",
    instructions=[
        "Recommend focus techniques, distraction blocking tools, and environment setup ideas.",
        "Offer break suggestions and app usage boundaries.",
        "Use DuckDuckGo if needed for the latest in productivity tools."
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

productivity_strategist = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Combines planning and focus recommendations into a single motivational strategy.",
    instructions=[
        "Merge time-based routines and focus tools into a practical, trackable plan.",
        "Use tables for clarity and highlight major vs minor tasks.",
        "Incorporate weekly and monthly vision alignment."
    ],
    markdown=True
)

# Streamlit Setup
st.set_page_config(page_title="AI Productivity Booster", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
        .title { text-align: center; font-size: 48px; font-weight: bold; color: #4CAF50; }
        .subtitle { text-align: center; font-size: 24px; color: #1976D2; margin-bottom: 30px; }
        .section-title { font-size: 20px; margin-top: 20px; color: #333; }
        .content-block { background-color: #f9f9f9; padding: 25px; border-radius: 12px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">🧠 AI Productivity Booster</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart daily, weekly, and monthly planning with AI agents.</p>', unsafe_allow_html=True)

# Sidebar for User Info
st.sidebar.header("👤 Your Profile")
name = st.sidebar.text_input("Your Name", value="Alex")
productivity_style = st.sidebar.selectbox("Work Style", ["Pomodoro", "Deep Work", "Balanced"])
distraction_level = st.sidebar.selectbox("Distraction Level", ["Low", "Moderate", "High"])

# Main content area for goal setting
st.markdown("<div class='section-title'>🎯 Planning Inputs</div>", unsafe_allow_html=True)
# st.markdown("<div class='content-block'>", unsafe_allow_html=True)
daily_goals = st.text_area("Major Goals for Today (comma-separated)", "Complete client presentation, Submit report")
minor_goals = st.text_area("Minor Tasks for Today", "Read 10 pages, Clean workspace")
weekly_plan = st.text_area("Weekly Vision", "Prepare slide deck, meet stakeholders, publish newsletter")
monthly_plan = st.text_area("Monthly Intentions", "Launch campaign, finalize product roadmap")
custom_prompt = st.text_area("🗣️ Additional Instructions (Optional)", "")
st.markdown("</div>", unsafe_allow_html=True)

# Generate Button
if st.button("🧩 Generate My Productivity Strategy"):
    with st.spinner("⏳ Creating your personalized plan..."):
        base_prompt = (
            f"User: {name}\n\nProductivity Style: {productivity_style}\nDistraction Level: {distraction_level}\n"
            f"Major Daily Goals: {daily_goals}\nMinor Tasks: {minor_goals}\n\n"
            f"Weekly Plan: {weekly_plan}\nMonthly Plan: {monthly_plan}\n"
        )

        if custom_prompt.strip():
            base_prompt += f"Additional Instructions: {custom_prompt}\n"

        routine = routine_builder.run(base_prompt)
        focus = focus_trainer.run(base_prompt)

        full_plan = productivity_strategist.run(
            f"{base_prompt}\n\nRoutine Plan:\n{routine}\n\nFocus Support:\n{focus}\n\nIntegrate all into one strategic plan."
        )

        st.subheader("📋 Your Smart Productivity Plan")
        st.markdown(full_plan.content)
        st.success("Plan ready! Let’s make today productive. 💼")
