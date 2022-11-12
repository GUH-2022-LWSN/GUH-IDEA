from database.load_json import load_data
from fastapi import FastAPI, HTTPException
from models.company import Company
from models.tweet import Tweet
from routers import round_robin
from internal.responses import AnswerResponse

app = FastAPI()
app.include_router(round_robin.router)

companies = load_data()

@app.get("/alive")
async def is_alive():
    return [{"Alive": True}]

@app.get("/getQuestion")
async def get_companies():
    return companies

@app.post("/submitResponse")
async def get_answer(response: AnswerResponse):
    company_id = response.company_id
    tweet_id = response.tweet_id

    if companies.get(company_id, False) is False:
         raise HTTPException(status_code=404, detail="Company with ID not found")
    
    company = companies[company_id]

    if company.correct_tweets.get(tweet_id, False):
        return {"answer": True}
    
    return {"answer": False}
    


