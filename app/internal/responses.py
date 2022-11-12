from pydantic import BaseModel

class AnswerResponse(BaseModel):
    company_id: str
    tweet_id: str