import streamlit as st
import numpy as np
import pickle
import os

# Load trained model
model = pickle.load(open("Downloads/UPSKILL/Machine_Learning/Insurance_premium_prediction.sav", "rb"))

# Title
st.title("Insurance Charge Predictor")

# Create input fields
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Convert categorical variables
sex_val = 1 if sex == "Male" else 0
smoker_val = 1 if smoker == "Yes" else 0
region_mapping = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
region_val = region_mapping[region]

# Predict charge
if st.button("Predict Insurance Charge"):
    input_features = np.array([[age, sex_val, bmi, children, smoker_val, region_val]])
    predicted_charge = model.predict(input_features)[0]
    st.success(f"Predicted Insurance Charge: INR. {predicted_charge:.2f}")
