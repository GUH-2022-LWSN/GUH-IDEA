from pydantic import BaseModel

class AnswerResponse(BaseModel):
    company_id: str
    tweet_id: str

class LeaderboardResponse(BaseModel):
    twitter_handle: str
    score: str
    level: int