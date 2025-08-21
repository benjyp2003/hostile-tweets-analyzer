from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.manager import Manager


class TweetResponse(BaseModel):
    """Simple response model for analyzed tweets"""
    processed_data: List[dict]

app = FastAPI()
manager = Manager()

@app.get("/")
async def read_root():
    try:
        return {"message": "Welcome to the Iran Tweets Analyzer API, use the endpoint /get_analyzed_data to get the analyzed tweets."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.get("/get_analyzed_data", response_model=TweetResponse)
async def get_analyzed_data():
    try:
        return manager.get_processed_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving analyzed data: {str(e)}")

@app.on_event("startup")
async def startup_event():
    try:
        manager.process_data()
        print("Data processing completed successfully")
    except Exception as e:
        print(f"Error during startup data processing: {e}")



