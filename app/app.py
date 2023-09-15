from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to ChatGPT API Wrapper!"
