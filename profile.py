import streamlit as st
from pymongo import MongoClient, errors

# MongoDB Connection
MONGO_URL = "mongodb://admin:password@mongodb:27017"


try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    db = client["my-db"]
    users_collection = db["users"]
    client.server_info()  # Trigger exception if connection fails
except errors.ServerSelectionTimeoutError:
    st.error("Could not connect to MongoDB. Ensure MongoDB is running on localhost:27017.")
    users_collection = None

def get_profile():
    if not users_collection:
        return {"name": "Anna Smith", "email": "anna.smith@example.com", "interests": "coding"}
    user = users_collection.find_one({"userid": 1}, {"_id": 0})
    return user if user else {"name": "Anna Smith", "email": "anna.smith@example.com", "interests": "coding"}

def update_profile(name, email, interests):
    if not users_collection:
        st.error("Database connection failed. Cannot update profile.")
        return
    user_data = {"userid": 1, "name": name, "email": email, "interests": interests}
    users_collection.update_one({"userid": 1}, {"$set": user_data}, upsert=True)
    return user_data

st.title("User Profile")

user = get_profile()
name = st.text_input("Name", user["name"])
email = st.text_input("Email", user["email"])
interests = st.text_input("Interests", user["interests"])

if st.button("Update Profile"):
    updated_user = update_profile(name, email, interests)
    if updated_user:
        st.success("Profile Updated Successfully!")
        st.write(updated_user)
