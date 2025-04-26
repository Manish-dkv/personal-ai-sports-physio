import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Function to fetch city suggestions
def get_city_suggestions(input_text):
    endpoint = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": input_text,
        "types": "(cities)",
        "key": GOOGLE_API_KEY
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    if data.get("status") == "OK":
        return [item["description"] for item in data["predictions"]]
    else:
        return []

# Streamlit UI
st.set_page_config(page_title="AI Sports Physio", page_icon="💪", layout="centered")
st.title("🏥 Personal AI Sports Physio")
st.subheader("Your pocket physiotherapist — powered by Generative AI")

# User Form
with st.form("user_info"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    city_input = st.text_input("Enter your City (Start Typing...)")

    city_suggestions = []
    if city_input:
        city_suggestions = get_city_suggestions(city_input)

    selected_city = st.selectbox("Suggested Cities:", city_suggestions) if city_suggestions else ""

    submit = st.form_submit_button("Submit")

if submit:
    if not (name and email and selected_city):
        st.warning("⚠️ Please fill in all the fields!")
    else:
        st.success(f"✅ Welcome {name}! Location set to {selected_city}")
        st.balloons()
