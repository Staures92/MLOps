import streamlit as st
import requests
import json

st.title('Churn Prediction App')

# Input fields for features
feature1 = st.number_input('Feature 1')
feature2 = st.number_input('Feature 2')
# ... other feature inputs

if st.button('Predict Churn'):
    # Prepare the data to send to the API
    data = {
        "feature1": feature1,
        "feature2": feature2,
        # ... other features
    }
    
    # Make a POST request to your API
    response = requests.post('http://localhost:8000/predict', json=data)
    
    if response.status_code == 200:
        result = response.json()
        st.write(f"Churn Probability: {result['churn_probability']:.2f}")
    else:
        st.error("Error occurred while making the prediction.")