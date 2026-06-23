import streamlit as st
import numpy as np
import pickle

# Load model (make sure model is saved already)
model = pickle.load(open("student_model.pkl", "rb"))

st.title("🎓 Student Score Predictor")
st.write("Predict your final marks based on inputs")

# Input fields
hours = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=80)
previous_score = st.number_input("Previous Score", min_value=0, max_value=100, value=70)

# Predict button
if st.button("Predict Score"):
    input_data = np.array([[hours, attendance, previous_score]])
    prediction = model.predict(input_data)

    st.success(f"🎯 Predicted Final Score: {prediction[0]:.2f}")