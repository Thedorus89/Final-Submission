from fastapi import FastAPI
from fastapi.responses import Response

from prometheus_client import Counter, Histogram, generate_latest

import time
import random

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

@app.get("/")
def home():

    REQUEST_COUNT.inc()

    start = time.time()

    prediction = random.randint(0, 1)

    PREDICTION_COUNT.inc()

    LATENCY.observe(time.time() - start)

    return {
        "prediction": prediction
    }

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )