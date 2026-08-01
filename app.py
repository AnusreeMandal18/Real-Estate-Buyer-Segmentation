# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:30:59 2026

@author: user
"""

import streamlit as st
import pandas as pd
import plotly.express as px

hide_streamlit_style = """
<style>

#MainMenu {
visibility: hidden;
}

footer {
visibility: hidden;
}

</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Configure page
st.set_page_config(
    page_title="Real Estate Market Intelligence",
    page_icon="🏢",
    layout="wide"
)

# ==========================================
# Font Styling
# ==========================================

st.markdown("""
<style>

/* Main Headings */
h1{
    font-family:"Dubai",sans-serif !important;
    font-size:46px !important;
    font-weight:700 !important;
}

h2{
    font-family:"Dubai",sans-serif !important;
    font-size:34px !important;
    font-weight:700 !important;
}

h3{
    font-family:"Dubai",sans-serif !important;
    font-size:28px !important;
    font-weight:700 !important;
}

/* Paragraphs only */
p{
    font-family:"Dubai",sans-serif !important;
    font-size:17px !important;
}

/* Markdown text */
[data-testid="stMarkdownContainer"]{
    font-family:"Dubai",sans-serif !important;
}

</style>
""", unsafe_allow_html=True)
    
# Load dataset
buyer_df = pd.read_csv("buyer_market_intelligence.csv")

# ==========================================
# Sidebar Navigation
# ==========================================

st.sidebar.title("🏢 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📊 Dashboard",
        "👤 Buyer Explorer",
        "ℹ️ About Project"
    ]
)
# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home":

    st.title("🏢 Real Estate Market Intelligence Dashboard")

    st.markdown("""
    ### Machine Learning Based Buyer Segmentation and Investment Profiling

    Welcome to the interactive dashboard developed to analyze buyer behaviour,
    investment patterns and customer segments in the real estate market using
    Machine Learning techniques.

    Use the navigation panel on the left to explore the dashboard.
    """)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Total Buyers", buyer_df.shape[0])

    with col2:
        st.metric("🏠 Properties Owned", buyer_df["properties_owned"].sum())

    with col3:
        st.metric(
            "💰 Average Investment ($)",
            f"{buyer_df['total_investment'].mean():,.2f}"
        )

    with col4:
        st.metric(
            "⭐ Average Satisfaction",
            f"{buyer_df['avg_satisfaction'].mean():.2f}"
        )


# ==========================================
# DASHBOARD PAGE
# ==========================================

elif page == "📊 Dashboard":

    st.title("📊 Buyer Analytics Dashboard")

    st.markdown("### Executive Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Total Buyers", buyer_df.shape[0])

    with c2:
        st.metric(
            "🏠 Properties Owned",
            int(buyer_df["properties_owned"].sum())
        )

    with c3:
        st.metric(
            "💰 Average Investment",
            f"${buyer_df['total_investment'].mean():,.2f}"
        )

    with c4:
        st.metric(
            "⭐ Average Satisfaction",
            f"{buyer_df['avg_satisfaction'].mean():.2f}/5"
        )

    st.divider()

    st.subheader("📈 Market Analytics")
    
    st.markdown("### 🌍 Buyer Distribution by Country & Region")

    st.write(
        """
      The USA contributes the highest proportion of buyers, followed by the UK. Buyer concentration is strongest in a few key regions, indicating high-potential markets for future customer acquisition and regional expansion.
        """
    )

    with st.expander("📈 Click to View Sunburst Chart"):

        region_data = (
            buyer_df.groupby(["country", "region"])
            .size()
            .reset_index(name="buyers")
    )

        fig = px.sunburst(
            region_data,
            path=["country", "region"],
            values="buyers",
            color="country",
            color_discrete_sequence=px.colors.qualitative.Pastel
    )

        fig.update_layout(
            width=800,
            height=900,
            margin=dict(t=60, l=20, r=20, b=20),
            font=dict(size=14)
    )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()

    st.markdown("### 👤 Client Type Distribution")

    st.write("""
             Individual buyers represent the largest share of the customer base, while company buyers account for a considerably smaller proportion. This distribution suggests that marketing efforts should primarily focus on individual investors while maintaining specialized services for corporate clients.
             """)

    with st.expander("📊 View Chart"):

        client_type_counts = (
            buyer_df["client_type"]
            .value_counts()
            .reset_index()
    )

        client_type_counts.columns = ["Client Type", "Count"]

        fig = px.pie(
            client_type_counts,
            names="Client Type",
            values="Count",
            hole=0.55,
            color_discrete_sequence=px.colors.qualitative.Pastel
    )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label"
    )

        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()

    st.markdown("### 💰 Investment Analysis")

    st.write("""
             Investment values are concentrated within a relatively consistent range, with only a limited number of buyers making significantly larger investments. This indicates the presence of a stable investment market alongside a smaller premium investment segment.
             """)

    with st.expander("📊 View Chart"):

        fig = px.box(
            buyer_df,
            y="total_investment",
            color_discrete_sequence=px.colors.qualitative.Set2
    )

        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()

    st.markdown("### ⭐ Customer Satisfaction Analysis")

    st.write("""
             Customer satisfaction remains relatively consistent across different client categories, indicating a stable customer experience. Although satisfaction levels do not vary significantly, maintaining service quality across all buyer groups remains essential for long-term customer retention.
             """)

    with st.expander("📊 View Chart"):

        fig = px.violin(
            buyer_df,
            x="client_type",
            y="avg_satisfaction",
            color="client_type",
            box=True,
            points="all",
            color_discrete_sequence=px.colors.qualitative.Set2
    )

        fig.update_layout(
            height=600
    )

        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()

    st.markdown("### 🤖 Buyer Segment Distribution")

    st.write("""
             The clustering algorithm identified four distinct buyer segments based on demographic characteristics and investment behaviour. These segments provide valuable insights for developing targeted marketing strategies and personalized investment recommendations.
             """)

    with st.expander("📊 View Chart"):

        segment_counts = (
            buyer_df["Buyer_Segment"]
            .value_counts()
            .reset_index()
    )

        segment_counts.columns = ["Buyer Segment", "Count"]

        fig = px.bar(
            segment_counts,
            x="Buyer Segment",
            y="Count",
            color="Buyer Segment",
            text="Count",
            color_discrete_sequence=px.colors.qualitative.Set2
    )

        fig.update_layout(height=550)

        st.plotly_chart(fig, use_container_width=True)
        
    st.divider()

    st.markdown("### 💰 Average Investment by Buyer Segment")

    st.write("""
             Investment behaviour differs across the identified buyer segments, reflecting varying purchasing capacities and investment objectives. Understanding these differences helps organizations tailor products and marketing efforts to each segment.
             """)

    with st.expander("📊 View Chart"):

        investment = (
            buyer_df.groupby("Buyer_Segment")["total_investment"]
            .mean()
            .reset_index()
    )

        fig = px.bar(
            investment,
            x="Buyer_Segment",
            y="total_investment",
            color="Buyer_Segment",
            text_auto=".2s",
            color_discrete_sequence=px.colors.qualitative.Pastel
    )

        fig.update_layout(height=550)

        st.plotly_chart(fig, use_container_width=True)     
        
    st.divider()

    st.markdown("### 😊 Average Satisfaction by Buyer Segment")

    st.write("""
             Average satisfaction levels remain fairly balanced across the four buyer segments, suggesting that the organization delivers a consistent customer experience irrespective of buyer profile.
             """)

    with st.expander("📊 View Chart"):

        satisfaction = (
            buyer_df.groupby("Buyer_Segment")["avg_satisfaction"]
            .mean()
            .reset_index()
    )

        fig = px.bar(
            satisfaction,
            x="Buyer_Segment",
            y="avg_satisfaction",
            color="Buyer_Segment",
            text_auto=".2f",
            color_discrete_sequence=px.colors.qualitative.Safe
    )

        fig.update_layout(height=550)

        st.plotly_chart(fig, use_container_width=True)    
        
    st.divider()

    st.markdown("### 📋 Strategic Recommendations")

    st.write("""
             The buyer segmentation results provide a foundation for designing more focused customer engagement strategies. Tailoring marketing campaigns, investment offerings and relationship management practices according to each buyer segment can improve decision-making and enhance overall business performance.
             """)

    with st.expander("📄 View Recommendations"):

        recommendations = buyer_df[
            ["Buyer_Segment", "Recommendation"]
            ].drop_duplicates()

        st.dataframe(
            recommendations,
            use_container_width=True
    )    
        
# ==========================================
# BUYER EXPLORER PAGE
# ==========================================

elif page == "👤 Buyer Explorer":

    st.title("👤 Buyer Explorer")

    st.write("Select a Buyer to explore their profile.")

    client = st.selectbox(
        "Choose Client ID",
        buyer_df["client_id"].sort_values().unique()
    )

    selected_buyer = buyer_df[buyer_df["client_id"] == client]

    st.success(f"Currently Viewing: {client}")

    st.write(f"**Client ID:** {client}")

    st.subheader("Buyer Profile")

    st.dataframe(selected_buyer)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("👤 Age", int(selected_buyer["Age"].iloc[0]))
        st.metric("🌍 Country", selected_buyer["country"].iloc[0])
        st.metric("📍 Region", selected_buyer["region"].iloc[0])
        st.metric("🏢 Client Type", selected_buyer["client_type"].iloc[0])

    with col2:
        st.metric(
            "🏠 Properties Owned",
            int(selected_buyer["properties_owned"].iloc[0])
        )

        st.metric(
            "💰 Total Investment ($)",
            f"{selected_buyer['total_investment'].iloc[0]:,.2f}"
        )

        st.metric(
    "⭐ Satisfaction",
    f"{selected_buyer['avg_satisfaction'].iloc[0]:.1f}/5"
)

        st.metric(
            "🎯 Acquisition Purpose",
            selected_buyer["acquisition_purpose"].iloc[0]
        )

# ==========================================
# ABOUT PROJECT PAGE
# ==========================================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About the Project")

    st.markdown("""
### Machine Learning Based Buyer Segmentation and Investment Profiling for Real Estate Market Intelligence

This dashboard was developed as part of a Machine Learning project to analyze buyer behaviour,
identify investment patterns and classify buyers into meaningful market segments using clustering techniques.

The project demonstrates how data-driven insights can support strategic decision-making,
customer segmentation and personalized marketing in the real estate industry.
""")

    st.divider()

    st.subheader("📌 Objectives")

    st.markdown("""
- Analyze buyer demographics and investment behaviour.
- Identify distinct buyer segments using Machine Learning.
- Explore investment and satisfaction patterns.
- Generate strategic recommendations for each buyer segment.
""")

    st.divider()

    st.subheader("🛠 Technologies Used")

    tech_df = pd.DataFrame({
        "Technology": [
            "Python",
            "Pandas",
            "NumPy",
            "Scikit-Learn",
            "Plotly",
            "Streamlit"
        ],
        "Purpose": [
            "Programming",
            "Data Processing",
            "Numerical Computing",
            "Machine Learning",
            "Interactive Visualizations",
            "Dashboard Development"
        ]
    })

    st.dataframe(
        tech_df,
        use_container_width=True
    )

    st.divider()

    st.subheader("🤖 Machine Learning Workflow")

    st.markdown("""
1. Data Collection

2. Data Cleaning

3. Feature Engineering

4. Exploratory Data Analysis

5. Feature Scaling

6. K-Means Clustering

7. Buyer Segmentation

8. Dashboard Development
""")

    st.divider()

    st.success("Developed as an academic Machine Learning project for Real Estate Market Intelligence.")

    