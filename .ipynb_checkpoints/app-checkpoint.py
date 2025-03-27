import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the prediction function
def predict_heart_disease(input_data):
    df = pd.DataFrame([input_data])  # Convert input to DataFrame
    prediction = model.predict(df)[0]
    if prediction == 1:
        return "Oh! The patient should visit the doctor. High Risk of Heart Disease."
    else:
        return "Good News! The patient doesn’t have heart disease. Low Risk of Heart Disease."

# Streamlit UI
st.title("Heart Disease Prediction App")
st.write("Enter patient details to predict heart disease risk.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=25)
sex = st.radio("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (CP)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", value=120)
chol = st.number_input("Cholesterol (chol)", value=200)
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", value=150)

# Convert categorical values
sex = 1 if sex == "Male" else 0

# Make prediction
if st.button("Predict"):
    user_input = {"age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol, "thalach": thalach}
    result = predict_heart_disease(user_input)
    st.success(result)
