import os
from fastapi import APIRouter

from ..database.leaderboard_service import load_leaderboard, save_leaderboard
from ..internal.responses import LeaderboardResponse

NUM_OF_ENTRIES = 5

def save():
    save_leaderboard(leaderboard)
        

router = APIRouter()
leaderboard = load_leaderboard()    

@router.get("/leaderboard")
async def get_leaderboard():
    return leaderboard

@router.post("/leaderboard/submit_entry", status_code=201)
def set_leaderboard(response: LeaderboardResponse):
    score = int(response.score)
    last_place = leaderboard["leaderboard"][NUM_OF_ENTRIES-1]

    if int(last_place["score"]) > score:
        return
    
    for i in range(NUM_OF_ENTRIES-2, -1, -1):
        place = leaderboard["leaderboard"][i]
        
        if score > int(place["score"]):
            continue

        result = {"twitter_handle": response.twitter_handle, "score": score, "level": response.level}
        leaderboard["leaderboard"].insert(i+1, result)

        if len(leaderboard["leaderboard"]) > NUM_OF_ENTRIES:
            leaderboard["leaderboard"].pop()  
        
        save_leaderboard(leaderboard)
        break
    else:
        result = {"twitter_handle": response.twitter_handle, "score": score, "level": response.level}
        leaderboard["leaderboard"].insert(0, result)
        if len(leaderboard["leaderboard"]) > NUM_OF_ENTRIES:
            leaderboard["leaderboard"].pop()  
        
        print(leaderboard)
        save_leaderboard(leaderboard)

    return ""
