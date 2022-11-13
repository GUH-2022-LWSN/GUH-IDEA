from pydantic import BaseModel
from typing import List, Dict

class RecordResponse(BaseModel):
    response: List[Dict[str, str]]

class AnswerResponse(BaseModel):
    company_id: str
    tweet_id: str

class LeaderboardResponse(BaseModel):
    twitter_handle: str
    score: str
    level: int