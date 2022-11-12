from pydantic import BaseModel
from datetime import date
from .tweet import Tweet

class Company(BaseModel):
        name: str
        handle: str
        picture: str | None
        followers: int
        following: int
        joined_date: date
        correct_tweets: list
        incorrect_tweets: list
