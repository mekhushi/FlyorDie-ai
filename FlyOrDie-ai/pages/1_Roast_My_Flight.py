import streamlit as st
import numpy as np
import pandas as pd
import joblib

# --- Page Title ---
st.markdown("<h1 style='text-align: center;'>🔥 Roast My Flight</h1>", unsafe_allow_html=True)
st.caption("Tell us about your flight... so we can tell you how badly it might end 😈")

# --- Load Model ---
try:
    model = joblib.load("model.pkl")
except:
    st.error("❌ Model file not found. Make sure 'model.pkl' is in the correct folder.")
    st.stop()

st.markdown("---")

# --- Input Form ---
st.markdown("### ✈️ Enter Your Flight Details")

with st.form("flight_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("🛫 Aircraft Age (Years)", 1, 50, 15)
        delay = st.slider("⏱️ Delay Rate (0.0 - 1.0)", 0.0, 1.0, 0.3)
        
    with col2:
        weather = st.slider("🌦️ Weather Score (1 = Stormy, 10 = Clear)", 1, 10, 6)
        maintenance = st.radio("🔧 Recent Maintenance Done?", ["Yes", "No"])
        maintenance = 1 if maintenance == "Yes" else 0

    submitted = st.form_submit_button("🛩️ Roast Me")

# --- Prediction ---
if submitted:
    input_data = np.array([[age, weather, delay, maintenance]])

    try:
        prediction = model.predict(input_data)[0]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.stop()

    roast_map = {
        0: ("✅ SAFE", "Smooth ride, probably. Just don't jinx it."),
        1: ("⚠️ RISKY", "Like a rickshaw on wings. Risky vibes."),
        2: ("💀 FATAL", "Make peace with your playlist. It’s your last one."),
    }

    risk_level, msg = roast_map.get(prediction, ("❓ UNKNOWN", "AI panicked. Take the train."))

    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>Risk Level: {risk_level}</h2>", unsafe_allow_html=True)
    st.info(msg)
