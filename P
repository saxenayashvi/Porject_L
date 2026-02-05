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

# Load the unified CSS for all pages
load_css(BASE / "merged-styles.css")

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
                <div class="button-container">
                    <a href="?page=choose_tool" class="begin-btn">Begin →</a>
                </div>
                <div class="footer">©️ 2024 EYGM Limited. All Rights Reserved.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RENDER: CHOOSE TOOL PAGE ----------------
elif current_page == "choose_tool":
    st.markdown('<div class="choose-tool-container">', unsafe_allow_html=True)
    st.markdown('<div class="tool-grid-wrapper">', unsafe_allow_html=True)
    
    st.markdown("# Choose Tool")
    
    # Create a proper grid layout
    st.markdown('<div class="tool-grid">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Tableau", key="tableau"):
            st.session_state["selected_tool"] = "Tableau"
            st.session_state["page"] = "configure"
            st.rerun()
    with col2:
        if st.button("SAP", key="sap"):
            st.session_state["selected_tool"] = "SAP"
            st.session_state["page"] = "configure"
            st.rerun()
    with col3:
        if st.button("Oracle", key="oracle"):
            st.session_state["selected_tool"] = "Oracle"
            st.session_state["page"] = "configure"
            st.rerun()
    
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("Qlik", key="qlik"):
            st.session_state["selected_tool"] = "Qlik"
            st.session_state["page"] = "configure"
            st.rerun()
    with col5:
        if st.button("Power BI", key="powerbi"):
            st.session_state["selected_tool"] = "Power BI"
            st.session_state["page"] = "configure"
            st.rerun()
    with col6:
        if st.button("Looker", key="looker"):
            st.session_state["selected_tool"] = "Looker"
            st.session_state["page"] = "configure"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close tool-grid
    st.markdown('</div>', unsafe_allow_html=True)  # Close tool-grid-wrapper
    
    if st.session_state.get("selected_tool"):
        st.success(f"You selected **{st.session_state['selected_tool']}**")
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close choose-tool-container

# ---------------- RENDER: CONFIGURE PAGE ----------------
elif current_page == "configure":
    # Render configure UI as a fresh page: do NOT show other tool buttons here.
    from frontend.tab_configure_app import render_configure_page

    selected_tool = st.session_state.get("selected_tool", "Tableau")
    render_configure_page(selected_tool)

else:
    # Fallback: go back to home
    st.session_state["page"] = "home"
    st.rerun()
