from fastapi import APIRouter, HTTPException
from random import choice, shuffle

from ..database.load_companies_tweets import load_data
from ..internal.responses import AnswerResponse

router = APIRouter()
companies, tweet_pairs, correct_tweets = load_data()

@router.get("/getQuestion")
async def get_companies():
    company_id = choice(list(companies.keys()))
    tweets = list(choice(tweet_pairs[company_id]))

    company = companies[company_id]
    shuffle(tweets)
    company.tweets = tweets

    return company


@router.post("/submitResponse")
async def get_answer(response: AnswerResponse):
    company_id = response.company_id
    tweet_id = response.tweet_id

    if correct_tweets.get(company_id, False) is False:
         raise HTTPException(status_code=404, detail="Company with ID not found")
    
    correct = correct_tweets[company_id]

    if correct.get(tweet_id, False):
        return {"answer": True}
    
    return {"answer": False}
