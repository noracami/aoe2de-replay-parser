import json
import logging
import os
from flask import Flask, request
from mgz.model import parse_match, serialize

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024  # 8 MB
if os.environ.get("LOG_LEVEL", "DEBUG") == "DEBUG":
    app.logger.setLevel(logging.DEBUG)
else:
    app.logger.setLevel(logging.INFO)


@app.get("/")
def hello_world():
    return "Hello, World!"


@app.post("/analyze_replay")
def analyze_replay():
    print(request.files)
    replay = request.files.get("replay")
    print(replay)

    if replay is None:
        return "You can provide a replay file", 200

    # Do something with the replay file
    match = parse_match(replay)
    data = json.dumps(serialize(match), indent=2)

    # return first 10 lines of the data
    return "\n".join(data.split("\n")[:10]), 200
