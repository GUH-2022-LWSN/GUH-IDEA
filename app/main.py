from database.load_json import load_data, get_file_hashes, get_saved_hash
from fastapi import FastAPI, HTTPException
from models.company import Company
from models.tweet import Tweet
from routers import round_robin
from internal.responses import AnswerResponse
from random import choice

app = FastAPI()
app.include_router(round_robin.router)

companies, tweet_pairs, correct_tweets = load_data()

@app.get("/alive")
async def is_alive():
    return [{"Alive": True}]

@app.get("/getQuestion")
async def get_companies():
    company_id = choice(list(companies.keys()))
    tweets = choice(tweet_pairs[company_id])

    company = companies[company_id]
    company.tweets = tweets

    return company


@app.post("/submitResponse")
async def get_answer(response: AnswerResponse):
    company_id = response.company_id
    tweet_id = response.tweet_id

    if correct_tweets.get(company_id, False) is False:
         raise HTTPException(status_code=404, detail="Company with ID not found")
    
    correct = correct_tweets[company_id]

    if correct.get(tweet_id, False):
        return {"answer": True}
    
    return {"answer": False}
