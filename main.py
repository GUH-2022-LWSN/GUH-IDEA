from fastapi import FastAPI
from routers import round_robin

app = FastAPI()

app.include_router(round_robin.router)

@app.get("/alive")
async def is_alive():
    return [{"Alive": True}]

