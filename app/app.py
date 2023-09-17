import os

import openai
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, UnsupportedMediaType
from models.chat_completion import ChatCompletionFactory

from constants import (ERROR_EMPTY_JSON, ERROR_INVALID_JSON,
                       ERROR_MISSING_MESSAGE, ERROR_UNSPORTED_MEDIA, SYSTEM_PROMPT, WELCOME_MESSAGE, ERROR_MISSING_MODEL)
from enums import Role

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize an empty list to store message history
messages_history = []


@app.route("/", methods=["GET"])
def welcome():
    return WELCOME_MESSAGE


@app.route("/chat", methods=["POST"])
def chat():
    is_valid, result = validate_request(request)

    if (not is_valid):
        return result

    message, model = result
    if (not messages_history):
        messages_history.append(SYSTEM_PROMPT)

    messages_history.append({"role": Role.USER.value, "content": message})
    factory = ChatCompletionFactory()

    try:
        chat_completion = factory.create_chat_completion(model)
        completion_message = chat_completion.generate_completion(
            messages_history)
        messages_history.append(completion_message)

        return jsonify(completion_message)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def validate_request(request):
    try:
        user_message = request.json
    except UnsupportedMediaType:
        # Not JSON request
        return False, (jsonify({"error": ERROR_UNSPORTED_MEDIA}), 415)
    except BadRequest:
        # Handle invalid JSON format
        return False, (jsonify({"error": ERROR_INVALID_JSON}), 400)

    if not user_message:
        return False, (jsonify({"error": ERROR_EMPTY_JSON}), 400)

    message = user_message.get("message")
    if not message:
        return False, (jsonify({"error": ERROR_MISSING_MESSAGE}), 400)

    model = user_message.get("model")
    if not model:
        return False, (jsonify({"error": ERROR_MISSING_MODEL}), 400)

    return True, (message, model)
