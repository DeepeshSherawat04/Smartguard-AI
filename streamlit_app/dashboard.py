import streamlit as st
from components.prediction_ui import render_prediction_ui
from components.report_ui import render_report_ui

st.set_page_config(
    page_title="SmartGuard AI",
    page_icon="🩺",
    layout="wide"
)

# ---------- Sidebar ----------
st.sidebar.title("🩺 SmartGuard AI")
st.sidebar.markdown("AI-powered healthcare system")

page = st.sidebar.radio(
    "Navigate",
    ["📊 Dashboard", "🔍 Disease Prediction", "📝 Report Analysis"]
)

# ---------- Dashboard ----------
if page == "📊 Dashboard":
    st.markdown("<h1>📊 SmartGuard AI Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("AI-powered preventive healthcare overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Diseases Supported", "Diabetes")

    with col2:
        st.metric("AI Modules", "ML + NLP")

    with col3:
        st.metric("System Status", "Running")

    st.info("Use the sidebar to navigate between modules.")

# ---------- Prediction ----------
elif page == "🔍 Disease Prediction":
    render_prediction_ui()

# ---------- Report Analysis ----------
elif page == "📝 Report Analysis":
    render_report_ui()