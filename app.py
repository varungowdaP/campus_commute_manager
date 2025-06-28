import streamlit as st

st.set_page_config(page_title="Campus Commute Manager", layout="wide")

st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["Add Ride", "Find Ride", "Manage Rides", "Dashboard"])

if page == "Add Ride":
    st.switch_page("pages/1_Add_Ride.py")
elif page == "Find Ride":
    st.switch_page("pages/2_Find_Ride.py")
elif page == "Manage Rides":
    st.switch_page("pages/3_Manage_Rides.py")
elif page == "Dashboard":
    st.switch_page("pages/4_Dashboard.py")
