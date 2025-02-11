from flask import Flask, request, jsonify, render_template
from app.chatbot import Chatbot

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
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
