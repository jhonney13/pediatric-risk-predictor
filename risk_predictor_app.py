import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load('risk_predictor_model.pkl')

# Diagnosis encoding
diagnosis_map = {'ASD': 0, 'VSD': 1, 'TOF': 2, 'PDA': 3}
reverse_risk_map = {0: 'High', 1: 'Low', 2: 'Medium'}
risk_color = {'High': '🔴', 'Medium': '🟠', 'Low': '🟢'}

# --- App Layout ---
st.set_page_config(page_title="Child Heart Surgery Risk Predictor", layout='centered')

st.markdown("<h1 style='text-align: center;'>🩺 Pediatric Post-Surgery Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict the risk of complications after congenital heart surgery</p>", unsafe_allow_html=True)
st.markdown("---")

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Child's Age (Years)", 0, 12, 3)
        weight = st.slider("Weight (kg)", 2.0, 30.0, 10.0)
        diagnosis = st.selectbox("Diagnosis Type", list(diagnosis_map.keys()))

    with col2:
        surgery_duration = st.slider("Surgery Duration (mins)", 60, 300, 120)
        oxygen_level = st.slider("Oxygen Saturation (%)", 80.0, 100.0, 95.0)
        heart_rate = st.slider("Heart Rate (bpm)", 80, 180, 120)

    submitted = st.form_submit_button("🧠 Predict Risk Level")

# Prediction logic
if submitted:
    diag_encoded = diagnosis_map[diagnosis]
    input_data = np.array([[age, weight, diag_encoded, surgery_duration, oxygen_level, heart_rate]])
    prediction = model.predict(input_data)[0]
    predicted_label = reverse_risk_map[prediction]
    emoji = risk_color[predicted_label]

    st.markdown("### 🔍 Prediction Result")
    st.success(f"{emoji} **Predicted Risk Level: {predicted_label}**")

    # Additional info box
    if predicted_label == 'High':
        st.error("⚠️ Immediate post-operative care is recommended. Prioritize ICU monitoring.")
    elif predicted_label == 'Medium':
        st.warning("🟠 Moderate risk. Follow-up observation needed.")
    else:
        st.info("🟢 Low risk. Standard post-operative care may be sufficient.")

# Footer
st.markdown("---")
st.markdown("<small>Developed for Sri Sathya Sai Sanjeevani Centre for Child Heart Care | Data Science Portfolio Project</small>", unsafe_allow_html=True)
