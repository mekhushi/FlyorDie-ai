import streamlit as st

# --- PAGE HEADER ---
st.markdown("<h1 style='text-align: center;'>📁 About This App</h1>", unsafe_allow_html=True)
st.caption("Because real-time sarcasm deserves a framework. 🛬")

# --- DESCRIPTION ---
st.markdown("""
### 🤖 What is FlyOrDie.ai?

This is a light-hearted ML-based web app that **predicts how risky your flight is** —  
not to actually save you, but mostly to entertain you before you board.  
It's part aviation… part AI… and part emotional damage.

---
""")

# --- FEATURES ---
st.markdown("### 🚀 What powers it?")
st.markdown("""
- **Model**: Random Forest Classifier  
- **Framework**: Streamlit  
- **Extras**: Pandas, NumPy, sarcasm, and coffee ☕  
""")

# --- FEATURES USED IN PREDICTION ---
st.markdown("### 📊 Model inputs")
st.markdown("""
- ✈️ Aircraft Age  
- 🌧️ Weather Conditions  
- ⏱️ Delay Rate  
- 🔧 Maintenance History  
""")

# --- WARNING ---
st.warning("⚠️ Disclaimer: This is for entertainment only. Not certified by aviation authorities, or even your parents.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align:center; font-size: 0.9em;'>Made with ❤️ by Khushiee — proudly roasting flights with AI.</div>", unsafe_allow_html=True)
