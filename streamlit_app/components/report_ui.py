import streamlit as st
import requests

def render_report_ui():
    st.markdown("<h1>📝 Medical Report Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("Analyze medical reports using AI.")

    report_text = st.text_area(
        "Paste medical report text",
        height=220,
        placeholder="Patient glucose levels are high and cholesterol is elevated..."
    )

    if st.button("🧠 Analyze Report"):
        if not report_text.strip():
            st.warning("Please enter report text.")
            return

        try:
            res = requests.post(
                "http://127.0.0.1:8000/analyze-report",
                json={"report_text": report_text}
            )
            data = res.json()

            st.subheader("📌 Key Findings")
            for item in data["report_summary"]:
                st.write("•", item)

        except Exception:
            st.error("Backend not reachable.")
