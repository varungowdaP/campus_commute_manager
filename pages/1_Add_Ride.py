import streamlit as st
from db.mongo_conn import rides_col

st.title("🚗 Post a New Ride")

# Form inputs
name = st.text_input("Your Name")
role = st.radio("You are a:", ["student", "recruiter"])
contact = st.text_input("Contact Number")

col1, col2 = st.columns(2)
with col1:
    source = st.text_input("From (Pickup Location)")
with col2:
    destination = st.text_input("To (Drop Location)")

time = st.time_input("Time of Ride")
seats = st.number_input("Available Seats", min_value=1, max_value=10)
status = st.selectbox("Ride Status", ["available", "full", "cancelled"])

# Add button
if st.button("Add Ride"):
    if all([name, role, contact, source, destination, time, seats, status]):
        ride_data = {
            "name": name,
            "role": role,
            "contact": contact,
            "from": source,
            "to": destination,
            "time": str(time),
            "seats_available": seats,
            "status": status
        }
        rides_col.insert_one(ride_data)
        st.success("✅ Ride posted successfully!")
    else:
        st.warning("⚠️ Please fill in all the details.")
