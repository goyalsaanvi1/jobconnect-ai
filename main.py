from flask import Flask, request, jsonify, render_template
from chatbot import run_mock_chat
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    response = run_mock_chat(user_input)
    return jsonify({"response": response})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)