import json
import os

LEADERBOARD_FILE = os.path.join(os.path.dirname(__file__), "leaderboard.json")

def load_leaderboard():
    leaderboard = open(LEADERBOARD_FILE, "r")

    leaderboard_data = json.loads(leaderboard.read())
    print(leaderboard_data)