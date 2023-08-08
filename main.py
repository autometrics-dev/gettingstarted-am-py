import time
import uvicorn

from fastapi import FastAPI, HTTPException, Response

from autometrics import autometrics
from autometrics.objectives import Objective, ObjectiveLatency, ObjectivePercentile

from prometheus_client import start_http_server, generate_latest


app = FastAPI()


API_SLO = Objective(
    "api",
    success_rate=ObjectivePercentile.P99_9,
    latency=(ObjectiveLatency.Ms250, ObjectivePercentile.P90),
)

@app.get("/")
@autometrics(objective=API_SLO)
async def read_root():
    return {"Hello": "World"}


@app.get("/error")
@autometrics(objective=API_SLO)
async def error_function():
    raise HTTPException(status_code=404, detail="Internal Server Error")

@app.get("/slow")
@autometrics(objective=API_SLO)
async def slow_function():
    time.sleep(2.4)
    return {"I am": "Slow"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest())

start_http_server(8080)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
