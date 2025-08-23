from flask import Flask, request, jsonify
from flask_cors import CORS

from api.consts import ADMIN_USER, ADMIN_PASS_HASH
from api.server_utils import ERROR_REDIRECT_HTML
from db.db_handler import add_client, list_clients, add_inventory_item, update_inventory_qty, add_order
from db.enums import PickupPlace, Unit


app = Flask(__name__)
origins = ["http://localhost:3000", "https://crust-and-crumb.vercel.app/"]
CORS(app, origins=origins)


@app.route('/')
def home():
    return ERROR_REDIRECT_HTML


@app.route('/login', methods=["POST"])
def login():
    body = request.json or {}

    username = body.get("username")
    password_hash = body.get("password")

    if not username or not password_hash:
        return jsonify({"success": False, "message": "Missing username or password"}), 400

    if username != ADMIN_USER:
        return jsonify({"success": False, "message": "Invalid username"}), 401

    if password_hash == ADMIN_PASS_HASH:
        return jsonify({"success": True}), 200

    return jsonify({"success": False, "message": "Invalid password"}), 401


# ---------- New endpoints using db_handler ----------
@app.route("/clients", methods=["POST"])
def create_client():
    data = request.json or {}
    try:
        client_id = add_client(
            name=data["name"],
            phone=data["phone"],
            pickup_place=PickupPlace[data["pickup_place"]],  # expects enum key
            notes=data.get("notes")
        )
        return jsonify({"success": True, "client_id": client_id}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/clients", methods=["GET"])
def get_clients():
    clients = list_clients()
    return jsonify([
        {"id": c.id, "name": c.name, "phone": c.phone, "pickup_place": c.pickup_place.value}
        for c in clients
    ])


@app.route("/inventory", methods=["POST"])
def add_inventory():
    data = request.json or {}
    try:
        item_id = add_inventory_item(
            ingredient=data["ingredient"],
            qty=data["qty"],
            unit=Unit[data["unit"]],  # expects enum key
            low_threshold=data.get("low_threshold", 0)
        )
        return jsonify({"success": True, "item_id": item_id}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory(item_id):
    data = request.json or {}
    new_qty = data.get("qty")
    updated = update_inventory_qty(item_id, new_qty)
    if updated:
        return jsonify({"success": True, "item_id": updated})
    return jsonify({"success": False, "message": "Item not found"}), 404


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json or {}
    try:
        order_id = add_order(
            client_id=data["client_id"],
            items=data["items"],  # list of {recipe_id, qty}
            pickup_date=data.get("pickup_date"),
            note=data.get("note")
        )
        return jsonify({"success": True, "order_id": order_id}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
