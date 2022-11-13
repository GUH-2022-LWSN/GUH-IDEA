from random import choice, shuffle
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import atexit
from .routers import round_robin, leaderboard   

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

@app.on_event("shutdown")
def shutdown_event():
    leaderboard.save()

@app.get("/alive")
async def is_alive():
    return [{"Alive": True}]

