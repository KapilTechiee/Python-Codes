import openai
from speech import speak

openai.api_key = "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"

def ask_chatgpt(question):
    """Ask ChatGPT and get a response"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response["choices"][0]["message"]["content"]

def chat_ai(command):
    """Use ChatGPT for conversation"""
    user_query = command.replace("chat", "").strip()
    ai_response = ask_chatgpt(user_query)
    speak(ai_response)
