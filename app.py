import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

st.title("Insurance Cost Prediction App")

st.sidebar.header("Input Features")

# Get user input for the features
age = st.sidebar.slider("Age", 18, 100, 30)
bmi = st.sidebar.slider("BMI", 15.0, 50.0, 25.0)
children = st.sidebar.number_input("Number of Children", 0, 10, 0)

# Categorical inputs
sex = st.sidebar.selectbox("Sex", ["male", "female"])
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Preprocess the input to match the model's expected format
# Our training script used one-hot encoding with drop_first=True. Hence, we need to create dummy variables accordingly.
input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "sex_male": [1 if sex == "male" else 0],
    "smoker_yes": [1 if smoker == "yes" else 0],
    # For 'region', assuming dummy variables for three of the four regions (with 'northeast' as the base)
    "region_northwest": [1 if region == "northwest" else 0],
    "region_southeast": [1 if region == "southeast" else 0],
    "region_southwest": [1 if region == "southwest" else 0],
})

if st.sidebar.button("Predict"):
    # Use the model to make a prediction
    prediction = model.predict(input_data)
    st.write(f"### Predicted Insurance Cost: ${prediction[0]:,.2f}")
