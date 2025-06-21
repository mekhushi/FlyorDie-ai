import streamlit as st
from datetime import datetime

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="FlyOrDie.ai",
    page_icon="🛬",
    layout="centered"
)

# ----- CUSTOM STYLE -----
st.markdown("""
    <style>
    .main {
        background-color: #f9fbfd;
    }
    h1, h2, h3 {
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: grey;
        margin-top: 40px;
    }
    .fun-box {
        background-color: #fff7e6;
        padding: 15px;
        border-left: 5px solid orange;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ----- HEADER -----
st.markdown("<h1>🛫 FlyOrDie.ai</h1>", unsafe_allow_html=True)
st.caption("AI that roasts your flight harder than your relatives roast your career choices.")

st.markdown("---")

# ----- FUN DESCRIPTION -----
st.markdown("### 🤔 Why FlyOrDie?")
st.markdown("""
Welcome to **FlyOrDie.ai** — the app that tells you what your pilot won’t.

Here’s what you can do:
- 🔥 **Roast your flight** based on safety stats  
- 📊 **Explore risk insights** in our dataset  
- 💀 **Cry a little** when you see the fatality probability  
- 💻 **Act smart** because it’s powered by ML (even if your airline isn’t)
""")

st.markdown("---")

# ----- HIGHLIGHT SECTION -----
st.markdown('<div class="fun-box">🚨 <strong>DISCLAIMER:</strong> This app is sarcastic. Do not use it for real flight decisions... unless you like chaos.</div>', unsafe_allow_html=True)

st.success("🎯 Use the sidebar to jump to: Roast My Flight, Risk Insights, or About.")

# ----- TECHNICALS -----
with st.expander("🔍 How it works (for nerds like us)"):
    st.markdown("""
    - Uses a **Random Forest Classifier** trained on simulated aviation data  
    - Input: Aircraft age, delay rate, weather score, maintenance flag  
    - Output: Risk category – Safe / Risky / Fatal  
    - Built with ❤️ using **Python, Pandas, Streamlit, and Sarcasm**
    """)

# ----- FOOTER -----
st.markdown(f"<div class='footer'>© {datetime.now().year} — Made by Khushiee 💖 with AI, memes & chai ☕</div>", unsafe_allow_html=True)
