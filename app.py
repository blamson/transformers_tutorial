# imports
import os
import json
from src.inference import load_model, predict
from flask import Flask, request, jsonify
from modules import schemas
from loguru import logger

app = Flask(__name__)
pipe = load_model(os.environ["SM_MODEL_DIR"])
# pipe = load_model("models/holding_zone/checkpoint-1756")


@app.route("/ping", methods=["GET"])
def ping():
    """
    Sanity check
    """

    return "pong"


@app.route("/invocations", methods=["POST"])
def invocations():
    """
    Handles prediction requests
    """

    body: dict = request.json

    if schemas.validate_request(body):
        data = body["strings"]
    else:
        error_response: dict = {
            "error": "Invalid Request",
            "message": "Invalid input format."
        }

        return jsonify(error_response), 400

    predictions: list = predict(data, pipe=pipe)
    output: str = json.dumps(predictions, indent=4)

    return output
