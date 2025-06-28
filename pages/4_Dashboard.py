import streamlit as st
import pandas as pd
import plotly.express as px
from db.mongo_conn import rides_col

st.set_page_config(layout="wide")
st.title("📊 Ride Insights Dashboard")

# Load all rides
rides = list(rides_col.find({}))
if not rides:
    st.warning("No rides to show.")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame(rides)

# Total rides metric
st.metric("Total Rides Posted", len(df))

# Row 1: Bar charts (From & To)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Pickup Locations")
    from_count = df["from"].value_counts().reset_index()
    from_count.columns = ["From", "Count"]
    fig1 = px.bar(from_count, x="From", y="Count", color="From", template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Top Destination Locations")
    to_count = df["to"].value_counts().reset_index()
    to_count.columns = ["To", "Count"]
    fig2 = px.bar(to_count, x="To", y="Count", color="To", template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

# Row 2: Status Donut Chart
st.subheader("Ride Status Distribution")
status_count = df["status"].value_counts().reset_index()
status_count.columns = ["Status", "Count"]
fig3 = px.pie(
    status_count,
    names="Status",
    values="Count",
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Pastel  # 👈 change as you like
)
st.plotly_chart(fig3, use_container_width=True)

# Optional: Time slot chart
st.subheader("Rides by Hour")
df["hour"] = pd.to_datetime(df["time"], errors="coerce").dt.hour
hour_count = df["hour"].value_counts().sort_index().reset_index()
hour_count.columns = ["Hour", "Count"]
fig4 = px.bar(hour_count, x="Hour", y="Count", template="plotly_dark", color="Count")
st.plotly_chart(fig4, use_container_width=True)
