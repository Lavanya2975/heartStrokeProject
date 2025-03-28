import streamlit as st
import pandas as pd
import joblib

# Load the trained model
with open("model.pkl", "rb") as file:
    model = joblib.load(file)

# Prediction logic
def predict_heart_disease(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return (
        "🩺 **High Risk:** The patient should consult a doctor immediately."
        if prediction == 1
        else "✅ **Low Risk:** The patient is not likely to have heart disease."
    )

# App UI setup
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.markdown("<h1 style='text-align: center;'>Heart Disease Prediction App</h1>", unsafe_allow_html=True)
st.markdown("Enter patient health information below to assess risk of heart disease.")

# Input form
with st.form("input_form"):
    age = st.number_input("Age", min_value=1, max_value=120)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200)
    chol = st.number_input("Serum Cholesterol (chol)", min_value=100, max_value=600)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
    restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved (thalach)", min_value=60, max_value=250)
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
    oldpeak = st.number_input("ST depression (oldpeak)", step=0.1, format="%.1f")
    slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

    submit = st.form_submit_button("Predict")

# Process input
if submit:
    # Prepare input in model format
    input_data = {
        "age": age,
        "sex": 1 if sex == "Male" else 0,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal,
    }
    result = predict_heart_disease(input_data)
    st.success(result)
