import os
import openai
from flask import Flask, jsonify, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize an empty list to store message history
messages_history = []

# System prompt to set initial behavior
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a friendly and adaptable conversational partner. Strive to provide engaging and helpful responses while maintaining a warm and approachable tone throughout the conversation."
}


def generate_completion(user_message):
    """Generate a completion using the user's message"""
    try:
        if (not messages_history):
            messages_history.append(SYSTEM_PROMPT)

        # Generate a completion using OpenAI APIs
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )

        # Assistant's message response
        completion_message = completion.choices[0].message

        # Add the assistant's response to the message history
        messages_history.append(completion_message)

        return completion_message
    except openai.error.OpenAIError as e:
        raise OpenAIError(str(e))


@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to ChatGPT API Wrapper!"


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Handle missing user message
    if not user_message:
        return jsonify({"error": "Missing 'message' in request JSON"}), 400

    try:
        completion_message = generate_completion(user_message)

        return jsonify(completion_message)
    except OpenAIError as e:
        return jsonify({"error": str(e)}), 500
