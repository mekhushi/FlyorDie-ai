import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Title ---
st.markdown("<h1 style='text-align: center;'>📊 Risk Insights</h1>", unsafe_allow_html=True)
st.caption("Because knowing how close to death your flight is should be a visual experience 😌")

# --- Load Data ---
try:
    df = pd.read_csv("FlyOrDie-ai/data/flight_sample_2022-09-01.csv.csv")
except Exception as e:
    st.error(f"⚠️ Could not load the dataset: {e}")
    st.stop()

# --- Check if necessary column exists ---
if "risk_label" not in df.columns:
    st.error("🧯 Missing column: 'risk_label'. Please check your CSV.")
    st.stop()

# --- Prepare Plot Data ---
counts = df["risk_label"].value_counts().sort_index()
labels = ["Safe", "Risky", "Fatal"]
colors = ["green", "orange", "red"]

# --- Plot ---
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x=labels, y=counts.values, palette=colors, ax=ax)
ax.set_title("🚦 Flight Risk Distribution (Training Data)")
ax.set_ylabel("Number of Flights")
ax.set_xlabel("Risk Category")

# --- Display Plot ---
st.pyplot(fig)

# --- Insight Message ---
st.markdown("---")
st.info("🔍 From the above data, you can see how often flights fall into each risk category. Green = Good. Red = …Not so much.")
