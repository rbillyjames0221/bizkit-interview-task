from flask import Blueprint, request, jsonify
from .data.search_data import USERS

bp = Blueprint("update_user", __name__, url_prefix="/users")

@bp.route("/<int:user_id>", methods=["PUT"])
def update_user_put(user_id):
    data = request.get_json()

    # Check if 'id' is in the request data
    if 'id' in data:
        return jsonify({"error": "Cannot update the ID field"}), 400

    for user in USERS:
        if user['id'] == str(user_id):
            user.update(data)
            return jsonify({"user": user,"message": "User updated successfully", }), 200

    return jsonify({"error": "User not found"}), 404

@bp.route("/<int:user_id>", methods=["PATCH"])
def update_user_patch(user_id):
    data = request.get_json()

    # Check if 'id' is in the request data
    if 'id' in data:
        return jsonify({"error": "Cannot update the ID field"}), 400

    for user in USERS:
        if user['id'] == str(user_id):
            user.update(data)
            return jsonify({"user": user,"message": "User updated successfully", }), 200

    return jsonify({"error": "User not found"}), 404

