from flask import Flask, request, jsonify, render_template
import sqlite3
from models.priority_model import predict_priority

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, title TEXT, description TEXT, priority INTEGER)''')
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data['title']
    description = data['description']
    priority = predict_priority(title, description)  # Predict priority
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)",
              (title, description, priority))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added successfully!"}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY priority DESC")
    tasks = c.fetchall()
    conn.close()
    return jsonify(tasks)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
