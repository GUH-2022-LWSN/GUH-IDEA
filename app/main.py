from random import choice

from database.load_json import load_data
from routers import round_robin
from internal.responses import AnswerResponse

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://justphish.tech",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
