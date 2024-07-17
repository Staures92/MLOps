import streamlit as st
import requests
import json

# Create the Streamlit app
def main():
    st.title("Churn Prediction App")
    
    # Input form
    monthly_charges = st.number_input("Monthly Charges:")
    total_charges_tenure = st.number_input("Total Charges Tenure:")
    total_charges = st.number_input("Total Charges:")
    internet_service = st.number_input("Internet Service:")
    partner = st.number_input("Partner:")
    multiple_lines = st.number_input("Multiple Lines:")
    device_protection = st.number_input("Device Protection:")
    senior_citizen = st.number_input("Senior Citizen:")
    gender = st.number_input("Gender:")
    online_backup = st.number_input("Online Backup:")
    dependents = st.number_input("Dependents:")
    tech_support = st.number_input("Tech Support:")
    online_security = st.number_input("Online Security:")
    phone_service = st.number_input("Phone Service:")
    contract = st.number_input("Contract:")
    tenure = st.number_input("Tenure:")
    
    # Predict button
    if st.button("Predict"):
        predict_churn(monthly_charges, total_charges_tenure, total_charges, internet_service, partner, 
                      multiple_lines, device_protection, senior_citizen, gender, online_backup, dependents, 
                      tech_support, online_security, phone_service, contract, tenure)  # Call the predict_churn function
        
    # Write a function called predict_churn that makes a POST request to the FastAPI endpoint to get the churn prediction
    def predict_churn(monthly_charges, total_charges_tenure, total_charges, internet_service, partner, multiple_lines, device_protection, senior_citizen, gender, online_backup, dependents, tech_support, online_security, phone_service, contract, tenure):
    # API endpoint
     api_endpoint = "http://your-fastapi-endpoint/predict_churn"
    
    # Request payload
    payload = {
        "MonthlyCharges": monthly_charges,
        "TotalCharges_Tenure": total_charges_tenure,
        "TotalCharges": total_charges,
        "InternetService": internet_service,
        "Partner": partner,
        "MultipleLines": multiple_lines,
        "DeviceProtection": device_protection,
        "SeniorCitizen": senior_citizen,
        "gender": gender,
        "OnlineBackup": online_backup,
        "Dependents": dependents,
        "TechSupport": tech_support,
        "OnlineSecurity": online_security,
        "PhoneService": phone_service,
        "Contract": contract,
        "tenure": tenure
    }
    
    try:
        # Make the API call
        response = requests.post(api_endpoint, json=payload)
        
        # Process the response
        if response.status_code == 200:
            result = response.json()
            churn_prediction = result["churn_prediction"]
            churn_probability = result["churn_probability"]
            
            st.write("Churn Prediction:", churn_prediction)
            st.write("Churn Probability:", churn_probability)
        else:
            st.error("Error occurred. Please try again.")
    except requests.exceptions.RequestException as e:
        st.error("Error occurred. Please try again.")
        
           # Run the streamlit App
        
        if __name__ == "__main__":
         main()
         
         
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

# Deploy your app to Heroku using the command: git push heroku master

# Once the deployment is complete, you can access your app using the URL provided by Heroku.

