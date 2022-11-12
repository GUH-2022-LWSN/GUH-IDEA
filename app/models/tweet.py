from pydantic import BaseModel
from datetime import datetime

class Tweet(BaseModel):
        body: str
        vibe: str | None
        retweets: int
        quote_tweets: int
        likes: int
        date: datetime
        attachment: str | None
