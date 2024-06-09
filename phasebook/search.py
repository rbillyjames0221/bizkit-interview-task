from flask import Blueprint, request, jsonify
from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("", methods=["GET"])
def search_users():
    search_params = request.args

    # Extract the query parameters in the order they are provided
    param_order = list(search_params.keys())

    # Assign scores dynamically based on the order of the parameters
    scores = {param: len(param_order) - idx for idx, param in enumerate(param_order)}

    def get_match_score(user):
        score = 0
        if 'id' in search_params and user['id'] == search_params['id']:
            score += scores.get('id', 0)
        if 'name' in search_params and search_params['name'].lower() in user['name'].lower():
            score += scores.get('name', 0)
        if 'age' in search_params and int(search_params['age']) - 1 <= user['age'] <= int(search_params['age']) + 1:
            score += scores.get('age', 0)
        if 'occupation' in search_params and search_params['occupation'].lower() in user['occupation'].lower():
            score += scores.get('occupation', 0)
        return score

    matching_users = [
        user for user in USERS
        if ('id' in search_params and user['id'] == search_params['id']) or
           ('name' in search_params and search_params['name'].lower() in user['name'].lower()) or
           ('age' in search_params and int(search_params['age']) - 1 <= user['age'] <= int(search_params['age']) + 1) or
           ('occupation' in search_params and search_params['occupation'].lower() in user['occupation'].lower())
    ]

    sorted_users = sorted(matching_users, key=get_match_score, reverse=True)
    return jsonify(sorted_users)
