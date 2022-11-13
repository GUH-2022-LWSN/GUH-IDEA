from pydantic import BaseModel
from datetime import datetime
from typing import Union

class Tweet(BaseModel):
        body: str
        vibe: Union[str, None]
        retweets: int
        quote_tweets: int
        likes: int
        date: datetime
        attachment: Union[str, None]
