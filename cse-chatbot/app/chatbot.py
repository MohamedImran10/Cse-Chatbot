import json
import google.generativeai as genai
from app.config import Config

class Chatbot:
    def __init__(self, responses_file="app/responses.json"):
        with open(responses_file, "r", encoding="utf-8") as file:
            self.data = json.load(file)

        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def get_response(self, query):
        # Check predefined responses first
        for item in self.data["questions"]:
            if query.lower() in item["question"].lower():
                return item["response"]

        # If not found, use Gemini AI
        return self.ask_gemini(query)

    def ask_gemini(self, query):
        try:
            response = self.model.generate_content(query)
            return response.text if response else "I'm not sure. Could you rephrase your question?"
        except Exception as e:
            return "Error: Unable to fetch response. Please try again later."
