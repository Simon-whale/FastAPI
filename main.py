import uvicorn
import json
import Services

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/results")
async def results():
    # While the code in these to calls are identical I want to
    # show the different ways of using the __init__ namespace
    return json.dumps(Services.DataGenerator.create())


@app.get("/results/")
async def results_dynamic(start: int = 0, end: int = 100):
    # While the code in these to calls are identical I want to
    # show the different ways of using the __init__ namespace
    return json.dumps(Services.generate_numbers(start, end))

# Automatically start the server on port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
