import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Healthcare Cost Dashboard", layout="wide", page_icon="🏥")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('clean_healthcare__dataset.csv')
    df = df[df['Billing Amount'] > 0]
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
medical_condition = st.sidebar.multiselect("Select Medical Condition", options=df['Medical Condition'].unique(), default=df['Medical Condition'].unique())
gender = st.sidebar.multiselect("Select Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
admission_type = st.sidebar.multiselect("Select Admission Type", options=df['Admission Type'].unique(), default=df['Admission Type'].unique())

# Filter data
filtered_df = df[
    (df['Medical Condition'].isin(medical_condition)) & 
    (df['Gender'].isin(gender)) & 
    (df['Admission Type'].isin(admission_type))
]

# Main Dashboard
st.title("🏥 Healthcare Cost & Patient Analysis Dashboard")
st.markdown("---")

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patients", f"{len(filtered_df):,}")
col2.metric("Avg Billing", f"${filtered_df['Billing Amount'].mean():,.2f}")
col3.metric("Total Revenue", f"${filtered_df['Billing Amount'].sum():,.2f}")
col4.metric("Avg Stay (Days)", f"{filtered_df['length_of_stay'].mean():.1f}")

st.markdown("---")

# Visualizations
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("💰 Billing Distribution by Medical Condition")
    fig = px.box(filtered_df, x="Medical Condition", y="Billing Amount", color="Medical Condition", 
                 title="Billing Amount Range per Condition")
    st.plotly_chart(fig, use_container_width=True)

with row1_col2:
    st.subheader("📊 Admission Type Distribution")
    fig = px.pie(filtered_df, names="Admission Type", title="Patient Volume by Admission Type", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("🏥 Top 10 Hospitals by Revenue")
    top_hospitals = filtered_df.groupby('Hospital')['Billing Amount'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top_hospitals, x='Billing Amount', y='Hospital', orientation='h', 
                 title="Top 10 High-Revenue Hospitals", color='Billing Amount', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

with row2_col2:
    st.subheader("⏳ Length of Stay vs. Billing Amount")
    fig = px.scatter(filtered_df.sample(min(2000, len(filtered_df))), x="length_of_stay", y="Billing Amount", 
                     color="Admission Type", hover_data=['Medical Condition'],
                     title="Stay Duration vs Cost (Sampled)")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("Created as part of the Healthcare Data Professional Portfolio Project.")
