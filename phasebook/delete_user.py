from flask import Blueprint, jsonify
from .data.search_data import USERS

bp = Blueprint("delete_user", __name__, url_prefix="/users")

@bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in USERS:
        if user['id'] == str(user_id):
            USERS.remove(user)
            return jsonify({
                "message": "User deleted successfully, below are the updated Users after deletion",
                "users": USERS
            }), 200
    return jsonify({"error": "User not found"}), 404