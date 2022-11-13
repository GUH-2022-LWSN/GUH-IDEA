from pydantic import BaseModel
from datetime import date
from .tweet import Tweet
from typing import Union

class Company(BaseModel):
        name: str
        handle: str
        picture: Union[str, None]
        followers: int
        following: int
        joined_date: date
        tweets = []
