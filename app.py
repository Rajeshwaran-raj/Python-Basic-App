from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

app = Flask(__name__)

# In-memory storage with some hard-coded values
ITEMS = {
    1: {"id": 1, "name": "Sample Item 1", "description": "First hard-coded item"},
    2: {"id": 2, "name": "Sample Item 2", "description": "Second hard-coded item"},
}
NEXT_ID = 3

def get_json_body():
    data = request.get_json(silent=True)
    if data is None:
        return {}
    return data

@app.get("/items")
def list_items():
    return jsonify(list(ITEMS.values())), 200

@app.post("/items")
def create_item():
    global NEXT_ID
    body = get_json_body()

    name = body.get("name")
    description = body.get("description", "")

    if not name:
        return jsonify({"error": "Field 'name' is required."}), 400

    item_id = NEXT_ID
    NEXT_ID += 1

    item = {"id": item_id, "name": name, "description": description}
    ITEMS[item_id] = item
    return jsonify(item), 201

@app.get("/items/<int:item_id>")
def get_item(item_id: int):
    item = ITEMS.get(item_id)
    if not item:
        return jsonify({"error": "Item not found."}), 404
    return jsonify(item), 200

@app.put("/items/<int:item_id>")
def update_item(item_id: int):
    item = ITEMS.get(item_id)
    if not item:
        return jsonify({"error": "Item not found."}), 404

    body = get_json_body()
    item["name"] = body.get("name", item["name"])
    item["description"] = body.get("description", item["description"])

    return jsonify(item), 200

@app.delete("/items/<int:item_id>")
def delete_item(item_id: int):
    item = ITEMS.get(item_id)
    if not item:
        return jsonify({"error": "Item not found."}), 404

    del ITEMS[item_id]
    return jsonify({"message": "Item deleted."}), 204


if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "True") == "True"

    app.run(host=host, port=port, debug=debug)
