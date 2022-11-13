from fastapi import APIRouter
from ..database.leaderboard_service import load_leaderboard
router = APIRouter()

@router.get("/leaderboard")
async def get_leaderboard():
    load_leaderboard()
    return ""

@router.post("/leaderboard/submit_entry")
def set_leaderboard():
    return ""