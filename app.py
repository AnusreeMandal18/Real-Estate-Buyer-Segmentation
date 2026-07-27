import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Real Estate Buyer Segmentation",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Machine Learning Based Buyer Segmentation")
st.subheader("Real Estate Market Intelligence System")

st.write(
    "This application predicts buyer segments using a trained "
    "Machine Learning model."
)

# Load model and scaler
model = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.success("✅ Model and Scaler loaded successfully!")
