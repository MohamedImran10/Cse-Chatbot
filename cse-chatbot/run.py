from flask import Flask, request, jsonify, render_template
from app.chatbot import Chatbot
import re

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")

chatbot = Chatbot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = chatbot.get_response(user_input)

    # Remove **bold** formatting
    clean_response = re.sub(r"\*\*(.*?)\*\*", r"\1", response)

    return jsonify({"response": clean_response})

if __name__ == "__main__":
    # Use PORT environment variable if available (for cloud deployments)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
