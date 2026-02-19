from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from joblib import load
import os

# Initialize app first
app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load(os.path.join(BASE_DIR, "model.pkl"))

class SalesData(BaseModel):
    cost: float
    price: float
    sold: int
    discount: float

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def predict(data: SalesData):
    profit = (data.price - data.cost) * data.sold
    revenue = data.price * data.sold
    margin = profit / revenue if revenue != 0 else 0

    

    features = [[
        data.cost,
        data.price,
        data.sold,
        data.discount,
        profit,
        margin
    ]]

    prediction = model.predict(features)[0]

    trend_map = {
        0: "Sales Going Down 📉",
        1: "Sales Stable ➖",
        2: "Sales Going Up 📈"
    }

    if prediction == 0 and profit < 500:
        advice = "Drop product or reduce cost"
    elif prediction == 0:
        advice = "Offer discount to boost sales"
    elif prediction == 1:
        advice = "Try small promotion"
    else:
        advice = "Continue selling and stock more"

    return {
        "profit": profit,
        "trend": trend_map[prediction],
        "recommendation": advice
    }

# steps to start
# cd backend

# python -m uvicorn main:app --reload
