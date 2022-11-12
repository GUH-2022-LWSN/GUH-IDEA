from fastapi import FastAPI
from routers import round_robin
from models.company import Company
from models.tweet import Tweet
from database.load_json import load_data

app = FastAPI()
app.include_router(round_robin.router)

companies = load_data()

@app.get("/alive")
async def is_alive():
    return [{"Alive": True}]

@app.get("/getQuestion")
async def get_companies():
    return companies

@app.get("/submitResponse"):


