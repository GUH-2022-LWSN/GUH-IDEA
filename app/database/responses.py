import json
import os

RESPONSES_FILE = os.path.join(os.path.dirname(__file__), "responses.json")

def load_respones():
    responses = open(RESPONSES_FILE, "r")

    response_data = json.loads(responses.read())
    return response_data

def save_responses(responses):
    writer = open(RESPONSES_FILE, "w")

    json.dump(responses, writer)
    writer.close()