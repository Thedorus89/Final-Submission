from fastapi import FastAPI
from fastapi.responses import Response

from prometheus_client import Counter, Histogram, generate_latest

import requests
import time

app = FastAPI()

REQUEST_COUNT = Counter(
    "request_count",
    "Total Request"
)

PREDICTION_COUNT = Counter(
    "prediction_count",
    "Total Prediction"
)

LATENCY = Histogram(
    "prediction_latency_seconds",
    "Prediction Latency"
)

MODEL_API_URL = "http://127.0.0.1:8000/predict"

@app.get("/")
def home():

    REQUEST_COUNT.inc()

    start = time.time()

    response = requests.get(MODEL_API_URL)

    prediction = response.json()

    PREDICTION_COUNT.inc()

    LATENCY.observe(time.time() - start)

    return prediction

@app.get("/predict")
def predict():

    prediction = 1

    return {
        "prediction": prediction
    }

@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type="text/plain"
    )