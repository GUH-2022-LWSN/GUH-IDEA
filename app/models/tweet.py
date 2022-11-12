from pydantic import BaseModel
from datetime import datetime

class Tweet(BaseModel):
        id_num: str
        body: str
        vibe: str | None
        retweets: int
        quote_tweets: int
        likes: int
        date: datetime
        attachment: str | None
