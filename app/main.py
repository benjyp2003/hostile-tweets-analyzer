from fastapi import FastAPI
import uvicorn

from app.manager import Manager
app = FastAPI()
manager = Manager()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tweets Analyzer API, use the endpoint /get_analyzed_data to get the analyzed data."}


@app.get("/get_analyzed_data")
def get_analyzed_data():
    return manager.get_processed_data()

@app.on_event("startup")
def startup_event():
    """
    This function is called when the application starts.
    It processes the data and stores it in the manager.
    """
    manager.process_data()


