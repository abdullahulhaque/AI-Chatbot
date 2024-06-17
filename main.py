from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Initialize OpenAI API key
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "----------------------------------------------------------------"))

def chat_with_openai(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    response = chat_with_openai(messages)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)