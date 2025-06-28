import streamlit as st
from db.mongo_conn import rides_col

st.title("🚌 Find a Ride")

# Search input
destination = st.text_input("Enter Destination (To)")
filter_status = st.selectbox("Status", ["available", "all"])
show_contact = st.checkbox("Show contact info")

# Search button
if st.button("Search"):
    if destination:
        query = {"to": {"$regex": destination, "$options": "i"}}
        if filter_status == "available":
            query["status"] = "available"

        results = list(rides_col.find(query))

        if results:
            st.success(f"✅ Found {len(results)} ride(s)")
            for ride in results:
                with st.expander(f"{ride['from']} ➝ {ride['to']} at {ride['time']}"):
                    st.markdown(f"👤 **Name:** {ride['name']}")
                    st.markdown(f"📍 **From:** {ride['from']}")
                    st.markdown(f"🏁 **To:** {ride['to']}")
                    st.markdown(f"🕒 **Time:** {ride['time']}")
                    st.markdown(f"🪑 **Seats:** {ride['seats_available']}")
                    st.markdown(f"📌 **Status:** `{ride['status']}`")
                    if show_contact:
                        st.markdown(f"📞 **Contact:** `{ride['contact']}`")
        else:
            st.warning("🚫 No rides found for this destination.")
    else:
        st.warning("⚠️ Please enter a destination.")
