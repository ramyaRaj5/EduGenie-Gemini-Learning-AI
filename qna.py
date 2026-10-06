import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_answer(question: str):
    prompt = f"Answer this question concisely: {question}"
    response = model.generate_content(prompt)
    return response.text