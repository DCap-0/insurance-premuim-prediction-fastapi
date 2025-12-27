import streamlit as st
import requests
from utils.config import get_api_url

API_URL = get_api_url()

st.set_page_config(
    page_title="Insurance Premium Predictor",
    layout="centered"
)

st.title("Insurance Premium Category Predictor")

# Input fields
age = st.number_input(
    label="Age",
    min_value=0,
    max_value=120,
    value=30
)
weight = st.number_input(
    label="Weight (kg)",
    min_value=0.1,
    value=45.5
)
height = st.number_input(
    label="Height (metres)",
    min_value=0.5,
    max_value=2.50,
    value=1.50
)
income_lpa = st.number_input(
    label="Income (lpa)",
    min_value=0.0,
    value=10.0
)
smoker = st.selectbox(
    label="Do you smoke?",
    options=["Yes", "No"]
)
city = st.text_input(
    label="City",
    value="Delhi"
)
occupation = st.selectbox(
    label="Occupation",
    options=['retired', 'freelancer', 'student', 'government_job',
             'business_owner', 'unemployed', 'private_job']
)

if smoker == "Yes":
    smoker = True
else:
    smoker = False

if st.button(label="Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(url=API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "response" in result:
            prediction = result['response']
            st.success(
                f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**"
            )
            st.write(f"Confidence: {prediction['confidence']}")
            st.write("Class Probabilities:")
            st.json(prediction['class_probabilities'])
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running.")
