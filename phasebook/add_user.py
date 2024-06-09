from flask import Blueprint, request, jsonify
from .data.search_data import USERS

bp = Blueprint("add_user", __name__, url_prefix="/users")

@bp.route("", methods=["POST"])
def add_user():
    new_user = request.get_json()
    USERS.append(new_user)
    return jsonify(new_user), 201
