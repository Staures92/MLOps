 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialize FastAPI app
app = FastAPI(title="Churn Prediction API")

# Load the trained model
model = joblib.load('rf_model.joblib')

# Load the scaler
scaler = joblib.load('scaler.joblib')

# Define input data model
class CustomerData(BaseModel): 
    MonthlyCharges: float
    TotalCharges_Tenure: float
    TotalCharges: float
    InternetService: int
    Partner: int
    MultipleLines: int
    DeviceProtection: int
    SeniorCitizen: int 
    gender: int
    OnlineBackup: int
    Dependents: int
    TechSupport: int
    OnlineSecurity: int
    PhoneService: int 
    Contract: int
    tenure: int 

# Define prediction endpoint
@app.post("/predict_churn")
async def predict_churn(customer: CustomerData):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([customer.dict()])
        
        # Preprocess the input data (scale features)
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)[0][1]  # Probability of churn
        
        return {
            "churn_prediction": bool(prediction[0]),
            "churn_probability": float(probability)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Churn Prediction API"}

 # To run the FastAPI application, run the following command in your terminal:
 # uvicorn backend:app --reload
 
 
  # This will start the server, typically at http://127.0.0.1:8000.
 # To test the API
  # Open a web browser and go to http://127.0.0.1:8000/docs. This will open the Swagger UI where you can test your API.
   # Click on the /predict_churn endpoint, then click "Try it out".
    #Enter sample customer data in the request body and execute the request.