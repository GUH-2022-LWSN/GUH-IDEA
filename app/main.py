from random import choice, shuffle
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import round_robin, leaderboard , responses  

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://justphish.tech",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(round_robin.router)
app.include_router(leaderboard.router)
app.include_router(responses.router)

@app.get("/alive")
async def is_alive():
    return [{"Alive": True}]

