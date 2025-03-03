import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset using a relative path
df = pd.read_csv("vehicles_dataset.csv")

st.title("Car Sales Dashboard")
st.write("Explore car sales data using interactive visualizations.")

# Display a sample of the data
if st.checkbox("Show Raw Data"):
    st.write(df.head())
