import os

import openai
from flask import Flask, jsonify, request
from config import CHAT_MODEL
from models.validator import Validator
from models.chat_completion import ChatCompletionFactory

from constants import SYSTEM_PROMPT, WELCOME_MESSAGE
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
    is_valid, result = Validator.chat_request_validator(request)

    if (not is_valid):
        return result

    message = result
    if (not messages_history):
        messages_history.append(SYSTEM_PROMPT)

    messages_history.append({"role": Role.USER.value, "content": message})

    try:
        chat_completion = ChatCompletionFactory.create_chat_completion(CHAT_MODEL)
        completion_message = chat_completion.generate_completion(
            messages_history)
        messages_history.append(completion_message)

        return jsonify(completion_message)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
