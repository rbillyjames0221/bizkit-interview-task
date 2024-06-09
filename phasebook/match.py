import time
from flask import Blueprint
from .data.match_data import MATCHES

bp = Blueprint("match", __name__, url_prefix="/match") #route for match id

@bp.route("/<int:match_id>") # handles route /match/<match_id>
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES): #validation if the match id is out of range or not
        return "Invalid match id", 404

    start = time.time() #records the start time
    #msg = "Match found" if is_match(*MATCHES[match_id]) else "No match" #call the function is_match and check 
    is_matched, matched_data = is_match(*MATCHES[match_id])
    end = time.time() #records the end time

    #added display matched data
    if is_matched:
        return {"message": "Match found", "matched_data": matched_data, "elapsedTime": end - start}, 200
    else:
        return {"message": "No match", "elapsedTime": end - start}, 200

def is_match(fave_numbers_1, fave_numbers_2): #ex. set1([1, 2, 3, 4],  set 2[2, 3]) ----> match_data.py
    set1 = set(fave_numbers_1)
    set2 = set(fave_numbers_2)
 
    #return set2.issubset(set1)

    matched_data = set2.intersection(set1) 
    return len(matched_data) > 0, list(matched_data) #display matched data
