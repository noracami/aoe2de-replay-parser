import json
from flask import Flask, request
from mgz.model import parse_match, serialize

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024  # 8 MB


@app.get("/")
def hello_world():
    return "Hello, World!"


@app.post("/analyze_replay")
def analyze_replay():
    replay = request.files.get("replay")
    if replay is None:
        return "You can provide a replay file", 200

    # Do something with the replay file
    match = parse_match(replay)
    data = json.dumps(serialize(match), indent=2)

    # return first 10 lines of the data
    return "\n".join(data.split("\n")[:10]), 200
