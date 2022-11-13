from fastapi import APIRouter
from ..database.leaderboard_service import load_leaderboard
router = APIRouter()

leaderboard = load_leaderboard()
@router.get("/leaderboard")
async def get_leaderboard():
    return leaderboard

@router.post("/leaderboard/submit_entry")
def set_leaderboard():
    return ""