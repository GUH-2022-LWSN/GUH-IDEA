import json
import os

LEADERBOARD_FILE = os.path.join(os.path.dirname(__file__), "leaderboard.json")

def load_leaderboard():
    leaderboard = open(LEADERBOARD_FILE, "r")

    leaderboard_data = json.loads(leaderboard.read())
    return leaderboard_data

def save_leaderboard(leaderboard):
    writer = open(LEADERBOARD_FILE, "w")

    json.dump(leaderboard, writer)
    writer.close()