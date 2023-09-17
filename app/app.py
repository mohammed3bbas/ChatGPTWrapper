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
    try:
        user_message = request.json
    except UnsupportedMediaType:
        # Not JSON request
        return jsonify({"error": ERROR_UNSPORTED_MEDIA}), 415
    except BadRequest:
        # Handle invalid JSON format
        return jsonify({"error": ERROR_INVALID_JSON}), 400

    if not user_message:
        return jsonify({"error": ERROR_EMPTY_JSON}), 400

    message = user_message.get("message")
    # Handle missing user message
    if not message:
        return jsonify({"error": ERROR_MISSING_MESSAGE}), 400

    model = user_message.get("model")
    if not model:
        return jsonify({"error": ERROR_MISSING_MODEL}), 400

    # Replace this with your GPT-3.5 Turbo code to generate the completion
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
