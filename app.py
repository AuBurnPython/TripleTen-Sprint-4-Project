import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page configuration
st.set_page_config(
    page_title="Car Sales Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load the dataset
df = pd.read_csv("vehicles_dataset.csv")

# Sidebar with filters
st.sidebar.header("Filter Data")
price_range = st.sidebar.slider("Select Price Range", int(df['price'].min()), int(df['price'].max()), (5000, 50000))
mileage_range = st.sidebar.slider("Select Mileage Range", int(df['odometer'].min()), int(df['odometer'].max()), (0, 150000))
selected_transmission = st.sidebar.multiselect("Select Transmission Type", options=df['transmission'].unique(), default=df['transmission'].unique())

# Filter the data based on user selection
filtered_df = df[(df['price'].between(*price_range)) & 
                 (df['odometer'].between(*mileage_range)) & 
                 (df['transmission'].isin(selected_transmission))]

# Main page title and description
st.title("🚗 Car Sales Dashboard")
st.markdown("""
    This dashboard allows you to explore car sales data with interactive filters. 
    Use the sidebar to adjust parameters and view the impact on the dataset.
""")

# Data Display
st.header("Data Overview")
st.dataframe(filtered_df, use_container_width=True)

# Plot 1: Price Distribution
st.header("Price Distribution of Cars")
fig1 = px.histogram(filtered_df, x="price", nbins=50, color="transmission", title="Car Price Distribution by Transmission Type")
st.plotly_chart(fig1, use_container_width=True)

# Plot 2: Price vs Mileage
st.header("Price vs. Mileage")
fig2 = px.scatter(filtered_df, x="odometer", y="price", color="transmission",
                  size="price", hover_data=["model"],
                  title="Price vs. Mileage of Cars")
st.plotly_chart(fig2, use_container_width=True)

# Optional: Show raw data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(filtered_df.head(20))
