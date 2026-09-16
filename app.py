from flask import Flask, render_template, request, jsonify
import sqlite3
from chatboot import get_response

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chats(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_reply TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_reply = get_response(user_message)

    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chats(user_message, bot_reply) VALUES (?, ?)",
        (user_message, bot_reply)
    )
    conn.commit()
    conn.close()

    return jsonify({"reply": bot_reply})

@app.route("/history")
def history():
    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()
    cur.execute("SELECT user_message, bot_reply FROM chats ORDER BY id")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)