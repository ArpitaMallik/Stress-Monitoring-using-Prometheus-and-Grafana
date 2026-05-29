import time

from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

requests_total = Counter("requests_total", "Total requests", ["path"])

request_duration = Histogram(
    "request_duration_seconds",
    "Request duration",
    ["path"],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1],
)

@app.get("/")
def home():
    start_time = time.time()

    requests_total.labels(path="/").inc()

    response = {"message": "Hello! I'm running."}

    duration = time.time() - start_time
    request_duration.labels(path="/").observe(duration)

    return response

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()