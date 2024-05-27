from flask import Blueprint, request, jsonify

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search_users(): 
    search_id = request.args.get('id')
    search_name = request.args.get('name', '').lower()
    search_age = request.args.get('age')
    search_occupation = request.args.get('occupation', '').lower()

    def get_match_score(user): #sort based on priority
        score = 0
        if search_id and user['id'] == search_id:
            score += 4  # Highest priority
        if search_name and search_name in user['name'].lower():
            score += 3
        if search_age and int(search_age) - 1 <= user['age'] <= int(search_age) + 1:
            score += 2
        if search_occupation and search_occupation in user['occupation'].lower():
            score += 1  # Lowest priority
        return score
    
    if search_id:  #id
        matching_users = [user for user in USERS if user['id'] == search_id]
    elif search_name: #name
        matching_users = [user for user in USERS if search_name in user['name'].lower()]
    elif search_age: #age
        matching_users = [user for user in USERS if int(search_age) - 1 <= user['age'] <= int(search_age) + 1]
    elif search_occupation: #occupation
        matching_users = [user for user in USERS if search_occupation in user['occupation'].lower()]
    elif search_id and search_name and not search_age and not search_occupation: #id and name
        matching_users = [user for user in USERS if user['id'] == search_id or search_name in user['name'].lower()]
    elif search_id and search_name and search_age and not search_occupation: #id, name, and age
        matching_users = [user for user in USERS if user['id'] == search_id or search_name in user['name'].lower() or int(search_age) - 1 <= user['age'] <= int(search_age) + 1]
    else: #id, name, age, occupation
        matching_users = [user for user in USERS if user['id'] == search_id or search_name in user['name'].lower() or int(search_age) - 1 <= user['age'] <= int(search_age) + 1 or search_occupation in user['occupation'].lower()]
    sorted_users = sorted(matching_users, key=get_match_score, reverse=True)
    return jsonify(sorted_users)
