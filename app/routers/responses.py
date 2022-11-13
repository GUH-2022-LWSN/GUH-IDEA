from fastapi import APIRouter, HTTPException

from ..database.load_companies_tweets import load_data
from ..database.responses import load_respones, save_responses
from ..internal.responses import RecordResponse

router = APIRouter()

from .round_robin import companies, tweet_pairs, correct_tweets, incorrect_tweets

@router.post("/responses")
async def record_response(response: RecordResponse):
    responses = response.response

    responses_db = load_respones()

    try:

        for resp in responses:
            company_id = resp["company_id"]

            if not correct_tweets[company_id].get(resp["tweet_id"], False) and not incorrect_tweets[company_id].get(resp["tweet_id"], False):
                raise HTTPException(status_code=404, detail="Company with ID not found")

            if correct_tweets[company_id].get(resp["tweet_id"], False):
                tweet = dict(correct_tweets[company_id].get(resp["tweet_id"], False))
                tweet["date"] = str(tweet["date"])
                
            if incorrect_tweets[company_id].get(resp["tweet_id"], False):
                tweet = dict(incorrect_tweets[company_id].get(resp["tweet_id"], False))
                tweet["date"] = str(tweet["date"])

            responses_db.append({
                "twitter_handle": resp["twitterHandle"],
                "company_id": resp["company_id"],
                "tweet": tweet,
                "action": resp["action"],
            })
        save_responses(responses_db)

        return 204
    except KeyError:
        raise HTTPException(status_code=500, detail="Something went wrong")
    
