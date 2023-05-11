from fastapi import FastAPI
import pandas as pd 
import uvicorn

df = pd.read_csv('./data/services2019.csv')

app = FastAPI()

@app.get("/")
def home(): 
    return {"this is a API service for MN drug summary details"}
    