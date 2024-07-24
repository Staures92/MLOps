import streamlit as st
import requests

# Define the FastAPI endpoint
url = "http://127.0.0.1:8000/predict_churn"

# Streamlit app
st.title("Churn Prediction App")

st.write("""
### Entrez les informations du client:
""")
# Input fields for customer data
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, format="%.2f")
TotalCharges_Tenure = st.number_input("Total Charges Tenure", min_value=0.0, format="%.2f")
TotalCharges = st.number_input("Total Charges", min_value=0.0, format="%.2f")
InternetService = st.selectbox("Internet Service", [0, 1, 2], format_func=lambda x: ["No", "DSL", "Fiber optic"][x])
Partner = st.selectbox("Partner", [0, 1], format_func=lambda x: ["No", "Yes"][x])
MultipleLines = st.selectbox("Multiple Lines", [0, 1], format_func=lambda x: ["No", "Yes"][x])
DeviceProtection = st.selectbox("Device Protection", [0, 1], format_func=lambda x: ["No", "Yes"][x])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: ["No", "Yes"][x])
gender = st.selectbox("Gender", [0, 1], format_func=lambda x: ["Female", "Male"][x])
OnlineBackup = st.selectbox("Online Backup", [0, 1], format_func=lambda x: ["No", "Yes"][x])
Dependents = st.selectbox("Dependents", [0, 1], format_func=lambda x: ["No", "Yes"][x])
TechSupport = st.selectbox("Tech Support", [0, 1], format_func=lambda x: ["No", "Yes"][x])
OnlineSecurity = st.selectbox("Online Security", [0, 1], format_func=lambda x: ["No", "Yes"][x])
PhoneService = st.selectbox("Phone Service", [0, 1], format_func=lambda x: ["No", "Yes"][x])
Contract = st.selectbox("Contract", [0, 1, 2], format_func=lambda x: ["Month-to-month", "One year", "Two year"][x])
tenure = st.number_input("Tenure", min_value=0, format="%d")

# When the 'Predict' button is clicked
if st.button("Predict"):
    # Prepare the input data
    input_data = {
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges_Tenure": TotalCharges_Tenure,
        "TotalCharges": TotalCharges,
        "InternetService": InternetService,
        "Partner": Partner,
        "MultipleLines": MultipleLines,
        "DeviceProtection": DeviceProtection,
        "SeniorCitizen": SeniorCitizen,
        "gender": gender,
        "OnlineBackup": OnlineBackup,
        "Dependents": Dependents,
        "TechSupport": TechSupport,
        "OnlineSecurity": OnlineSecurity,
        "PhoneService": PhoneService,
        "Contract": Contract,
        "tenure": tenure
    }
    
    # Send a POST request to the FastAPI endpoint
    response = requests.post(url, json=input_data)
    
    # Display the result
    if response.status_code == 200:
        result = response.json()
        st.write("### Prediction Result")
        st.write(f"Churn Prediction: {'Yes' if result['churn_prediction'] else 'No'}")
        st.write(f"Churn Probability: {result['churn_probability']:.2f}")
    else:
        st.write("Error:", response.status_code, response.text)
         
           # Deploy the Streamlit app
          # To deploy the Streamlit app, you can use various platforms like Heroku, AWS, or Streamlit Sharing.
           # we will be deploying to Heroku:

# Sign up for a Heroku account at https://signup.heroku.com/.
# Install the Heroku CLI by following the instructions provided in the Heroku documentation.
# Create a requirements.txt file in your project directory. This file should contain the necessary dependencies for your Streamlit app.
# Create a Procfile in your project directory. This file specifies the command to start your Streamlit app. For example, if your main Streamlit
# app file is called streamlit_app.py, the Procfile should contain:
#  web: streamlit run streamlit_app.py





 # Initialize a new Git repository in your project directory (if not already initialized) using the command: git init

# Add your files to the Git repository using the command: git add .
# Commit your changes using the command: git commit -m "Initial commit"

# Log in to your Heroku account using the command: heroku login

# Create a new Heroku app using the command: heroku create <app-name>(mine was megang-churn-app)
 # enter this command: heroku    git:remote    -a staures-churn-app

# Deploy your app to Heroku using the command: git push heroku master

# Once the deployment is complete, you can access your app using the URL provided by Heroku.

