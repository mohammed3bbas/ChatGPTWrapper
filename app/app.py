import os
import openai
from flask import Flask, jsonify, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

messages_history = []


@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to ChatGPT API Wrapper!"


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if (not messages_history):
        messages_history.append({
            "role": "system",
            "content": "You are a friendly and adaptable conversational partner. Strive to provide engaging and helpful responses while maintaining a warm and approachable tone throughout the conversation."
        })
    messages_history.append({"role": "user", "content": user_message})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages_history,
    )

    completion_message = completion.choices[0].message
    messages_history.append(completion_message)

    return jsonify(completion_message)
