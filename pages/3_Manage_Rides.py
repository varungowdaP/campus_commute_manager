import streamlit as st
from db.mongo_conn import rides_col
from bson import ObjectId

st.title("🛠️ Manage Your Rides")

# Ask for user name to fetch only their rides
user_name = st.text_input("Enter your name to manage your rides")

if user_name:
    my_rides = list(rides_col.find({"name": user_name}))

    if not my_rides:
        st.info("You haven't posted any rides yet.")
    else:
        st.success(f"Found {len(my_rides)} ride(s).")

        for ride in my_rides:
            with st.expander(f"{ride['from']} ➝ {ride['to']} at {ride['time']}"):
                # Editable fields
                new_from = st.text_input("From", value=ride['from'], key=f"from_{ride['_id']}")
                new_to = st.text_input("To", value=ride['to'], key=f"to_{ride['_id']}")
                new_time = st.time_input("Time", value=st.time_input("dummy", key=f"dummy_time_{ride['_id']}") if not ride['time'] else st.time_input("dummy", value=st.time_input("dummy", key=f"dummy2_{ride['_id']}")), key=f"time_{ride['_id']}") if False else st.time_input("Time", key=f"real_time_{ride['_id']}")
                new_seats = st.number_input("Seats", value=ride['seats_available'], min_value=1, max_value=10, key=f"seats_{ride['_id']}")
                new_status = st.selectbox("Status", ["available", "full", "cancelled"], index=["available", "full", "cancelled"].index(ride["status"]), key=f"status_{ride['_id']}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Update", key=f"update_{ride['_id']}"):
                        rides_col.update_one(
                            {"_id": ObjectId(ride["_id"])},
                            {"$set": {
                                "from": new_from,
                                "to": new_to,
                                "time": str(new_time),
                                "seats_available": new_seats,
                                "status": new_status
                            }}
                        )
                        st.success("✅ Ride updated successfully!")
                        

                with col2:
                    if st.button("Delete", key=f"delete_{ride['_id']}"):
                        rides_col.delete_one({"_id": ObjectId(ride["_id"])})
                        st.warning("🗑️ Ride deleted.")
                       
