# Heart Rate Variability (HRV) Anomaly Detection for Pediatric Heart Patients

## Project Overview
This project demonstrates a reproducible data science pipeline for analyzing Heart Rate Variability (HRV) in pediatric heart patients. The goal is to detect anomalies in heart rate that could indicate post-surgery complications, using simulated (synthetic) heart rate data.

The notebook simulates heart rate time-series data, injects artificial anomalies, visualizes the signal, applies smoothing, extracts frequency components, and detects anomalies using statistical methods.

## Pediatric Post-Surgery Risk Predictor App

This app is an interactive web tool designed to predict the risk of complications in children after congenital heart surgery. Built with Streamlit, it uses a machine learning model trained on pediatric surgery data to estimate the risk level (Low, Medium, or High) based on key clinical features.

### How the App Works
- **User Input:** The user enters patient details such as age, weight, diagnosis type, surgery duration, oxygen saturation, and heart rate through an intuitive form.
- **Prediction:** Upon submission, the app processes the input and uses a pre-trained model to predict the risk level of post-surgical complications.
- **Result Display:** The predicted risk (with a color-coded indicator) is shown instantly, along with tailored recommendations for post-operative care.

### How This App is Helpful
- **Clinical Decision Support:** Assists healthcare professionals in quickly assessing risk and prioritizing care for pediatric heart surgery patients.
- **User-Friendly:** The web interface is easy to use for clinicians, researchers, and students.
- **Educational Value:** Demonstrates the application of data science and machine learning in real-world healthcare scenarios.
- **Customizable:** Can be adapted to new data or additional features for broader clinical use.

## Features
- **Simulated Heart Rate Data:** 5 minutes of heart rate (BPM) data with realistic sinusoidal HRV and Gaussian noise.
- **Anomaly Injection:** Artificial spikes and drops to mimic clinical complications (e.g., tachycardia, bradycardia).
- **Visualization:** Clear time-series plots with anomalies highlighted.
- **Smoothing:** Moving average smoothing for trend analysis.
- **Frequency Analysis:** Fast Fourier Transform (FFT) to extract HRV frequency components.
- **Anomaly Detection:**
  - Z-score method
  - (Optional) IQR method
- **Healthcare Relevance:** Designed for junior data scientists in pediatric cardiology settings.

## Requirements
- Python 3.7+
- Standard data science libraries:
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - scipy
  - (optional) scikit-learn

All code blocks are commented for clarity and learning.

## Interpretation of Results
- **Anomalies:**
  - Red dots on plots indicate detected anomalies (sudden spikes/drops in heart rate).
  - These may correspond to clinical events such as arrhythmias or post-surgery complications.
- **Frequency Analysis:**
  - FFT plots help identify dominant HRV frequencies (e.g., respiratory sinus arrhythmia).
- **Adaptability:**
  - The pipeline can be adapted to real patient data for clinical or research use.

---

*For questions or improvements, please contact the project maintainer.* 
