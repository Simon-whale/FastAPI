import uvicorn
import json

from fastapi import FastAPI
from Services.GenerateData import DataGenerator

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/results")
async def results():
    worker = DataGenerator()
    return json.dumps(worker.create())


@app.get("/results/")
async def results_dynamic(start: int = 0, end: int = 100):
    worker = DataGenerator()
    return json.dumps(worker.create(start, end))

# Automatically start the server on port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
