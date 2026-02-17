from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder="static")

API_KEY = os.getenv("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")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("message")

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "arcee-ai/trinity-large-preview:free",
                "messages": [
                    {
                        "role": "system",
                        "content": "Ти — ШІ помічник Юр для сервера UKRAINE RP. Допомагай розбиратися в правилах, RP термінах та ситуаціях. Якщо питання не про RP — ввічливо відмов."
                    },
                    {
                        "role": "user",
                        "content": user_text
                    }
                ]
            }
        )

        data = r.json()
        reply = data["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Помилка сервера. Спробуйте пізніше."})

if __name__ == "__main__":
    app.run(debug=True)
