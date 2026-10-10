from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" — resets every time the app restarts.
# Good enough for a demo app; not meant for real persistence.
tasks = [
    {"id": 1, "title": "Learn Docker", "done": False},
    {"id": 2, "title": "Set up CI/CD", "done": False},
]


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps demo API is running",
        "endpoints": ["/health", "/tasks", "/tasks/<id>"]
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "task not found"}), 404
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "task not found"}), 404

    data = request.get_json() or {}
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
