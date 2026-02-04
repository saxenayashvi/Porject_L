import streamlit as st
from pathlib import Path

# ---------------- PAGE CONFIG (must be first) ----------------
st.set_page_config(
    page_title="BI4BI - EY Landing Page",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- LOAD CSS (by page) ----------------
def load_css(file_path: Path) -> None:
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

BASE = Path(__file__).parent

# ---------------- SESSION STATE: which page to show ----------------
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Navigate to Choose Tool when "Begin" link is clicked (query param)
if st.query_params.get("page") == "choose_tool" and st.session_state.get("page") != "choose_tool":
    st.session_state["page"] = "choose_tool"
    st.query_params.clear()
    st.rerun()

current_page = st.session_state["page"]

# Load the right CSS for the current page
if current_page == "home":
    load_css(BASE / "style.css")
else:
    load_css(BASE / "static" / "styles.css")

# ---------------- RENDER: LANDING PAGE (BI4BI) – single HTML card (rectangle) ----------------
if current_page == "home":
    st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 2.5, 1])

    with col_center:
        # Entire card as ONE div so we control shape (strict rectangle)
        st.markdown(
            """
            <div class="landing-card">
                <div class="title">BI4BI</div>
                <div class="desc">
                    BI4BI helps analyze existing BI reports, identify redundancies,
                    and provide recommendations to rationalize and modernize<br>
                    legacy BI environments using metadata-driven insights.
                </div>
                <a href="?page=choose_tool" class="begin-btn">Begin-&gt;</a>
                <div class="footer">©️ 2024 EYGM Limited. All Rights Reserved.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RENDER: CHOOSE TOOL PAGE ----------------
else:
    st.markdown("# Choose Tool")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Tableau"):
            st.session_state["selected_tool"] = "Tableau"
            st.rerun()
    with col2:
        if st.button("Oracle"):
            st.session_state["selected_tool"] = "Oracle"
            st.rerun()
    with col3:
        if st.button("Power BI"):
            st.session_state["selected_tool"] = "Power BI"
            st.rerun()

    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("SAP"):
            st.session_state["selected_tool"] = "SAP"
            st.rerun()
    with col5:
        if st.button("Qlik"):
            st.session_state["selected_tool"] = "Qlik"
            st.rerun()
    with col6:
        if st.button("Looker"):
            st.session_state["selected_tool"] = "Looker"
            st.rerun()

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    back_left, back_center, back_right = st.columns(3)
    with back_center:
        if st.button("← Back to Home"):
            st.session_state["page"] = "home"
            if "selected_tool" in st.session_state:
                del st.session_state["selected_tool"]
            st.rerun()

    if st.session_state.get("selected_tool"):
        st.success(f"You selected **{st.session_state['selected_tool']}**")
