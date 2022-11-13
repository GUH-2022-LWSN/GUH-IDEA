from pydantic import BaseModel
from datetime import date
from .tweet import Tweet
from typing import Union

class Company(BaseModel):
        company_id: str
        name: str
        handle: str
        picture: Union[str, None]
        followers: int
        following: int
        joined_date: date
        tweets = []
