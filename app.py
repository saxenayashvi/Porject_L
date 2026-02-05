import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BI4BI - EY Landing Page",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("background.png")
logo = get_base64("ey_logo.png")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

html, body {{
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    font-family: Arial, sans-serif;
}}

body {{
    background: url("data:image/png;base64,{bg}") no-repeat center center fixed;
    background-size: cover;
}}

/* HEADER */
.header {{
    position: fixed;
    top: 30px;
    left: 60px;
    right: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.title {{
    font-size: 26px;
    font-weight: 600;
    color: #000;
}}

.logo img {{
    width: 140px;
}}

/* CENTER CARD */
.center {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}}

.card {{
    background: white;
    width: 460px;
    padding: 42px;
    border-radius: 18px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    text-align: center;
}}

.card h1 {{
    font-size: 32px;
    margin-bottom: 20px;
    color: #333;
}}

/* TEXT CONTENT */
.desc {{
    font-size: 15px;
    color: #555;
    line-height: 1.6;
    margin-bottom: 28px;
}}

/* BUTTON */
.begin {{
    background: #FFD100;
    border: none;
    width: 100%;
    padding: 14px;
    font-size: 18px;
    font-weight: 600;
    border-radius: 10px;
    cursor: pointer;
}}

.begin:hover {{
    background: #f2c400;
}}

/* FOOTER */
.footer {{
    margin-top: 24px;
    font-size: 12px;
    color: #999;
}}
</style>
</head>

<body>
    <div class="header">
        <div class="title">BI4BI – EY Landing Page</div>
        <div class="logo">
            <img src="data:image/png;base64,{logo}" />
        </div>
    </div>

    <div class="center">
        <div class="card">
            <h1>BI4BI</h1>

            <p class="desc">
                abcd texttt paragraph abcd texttt paragraph abcd texttt paragraph.
                This text is only for demonstration and layout purposes.
                It represents static informational content on the BI4BI landing page
                without any form inputs or user interaction.
            </p>

            <button class="begin">Begin</button>

            <div class="footer">
                © 2024 EYGM Limited. All Rights Reserved.
            </div>
        </div>
    </div>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
