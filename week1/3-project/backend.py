 
    
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the model
model = joblib.load('churn_model.joblib')

class ChurnPredictionRequest(BaseModel):
    # Define your input features here
    feature1: float
    feature2: float
    # ... other features

class ChurnPredictionResponse(BaseModel):
    churn_probability: float

@app.post("/predict", response_model=ChurnPredictionResponse)
async def predict_churn(request: ChurnPredictionRequest):
    # Convert input to numpy array
    features = np.array([[
        request.feature1,
        request.feature2,
        # ... other features
    ]])
    
    # Make prediction
    churn_probability = model.predict_proba(features)[0][1]
    
    return ChurnPredictionResponse(churn_probability=float(churn_probability))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)