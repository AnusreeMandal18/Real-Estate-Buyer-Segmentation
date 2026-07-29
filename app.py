import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Real Estate Buyer Segmentation",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏠 Machine Learning Based Buyer Segmentation")
st.subheader("Investment Profiling for Real Estate Market Intelligence")

st.markdown("""
This application demonstrates a machine learning framework for buyer segmentation
using K-Means Clustering to analyze investment behaviour in the real estate market.
""")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("buyer_market_intelligence.csv")
st.write("Columns detected:")
st.write(df.columns.tolist())

# Load trained files
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.success("Project loaded successfully!")

st.write("### Dataset Preview")
st.dataframe(df.head())

st.write("### Dataset Shape")
st.write(df.shape)
