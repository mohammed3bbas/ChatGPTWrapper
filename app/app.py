import os

import openai
from flask import Flask, jsonify, request
from openai.error import OpenAIError
from werkzeug.exceptions import BadRequest, UnsupportedMediaType

from constants import (ERROR_EMPTY_JSON, ERROR_INVALID_JSON,
                       ERROR_MISSING_MESSAGE, ERROR_UNSPORTED_MEDIA,
                       GPT_3_5_TURBO_MODEL, SYSTEM_PROMPT, WELCOME_MESSAGE)
from enums import Role

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize an empty list to store message history
messages_history = []


def generate_completion(user_message):
    """Generate a completion using the user's message"""
    if (not messages_history):
        messages_history.append(SYSTEM_PROMPT)

    messages_history.append({"role": Role.USER.value, "content": user_message})

    try:
        # Generate a completion using OpenAI APIs
        completion = openai.ChatCompletion.create(
            model=GPT_3_5_TURBO_MODEL,
            messages=messages_history,
        )

        # Assistant's message response
        completion_message = completion.choices[0].message

        # Add the assistant's response to the message history
        messages_history.append(completion_message)

        return completion_message
    except OpenAIError as e:
        raise OpenAIError(str(e))


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

    user_message = user_message.get("message")
    # Handle missing user message
    if not user_message:
        return jsonify({"error": ERROR_MISSING_MESSAGE}), 400

    try:
        completion_message = generate_completion(user_message)
        return jsonify(completion_message)
    except OpenAIError as e:
        return jsonify({"error": str(e)}), 500
