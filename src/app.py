"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Response
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/member/<int:member_id>', methods=['GET', 'DELETE'])
def handle_member_by_id(member_id):
        
    id = member_id

    if request.method == 'GET':
        response_body = jackson_family.get_member(id)
        if response_body == None:
            return jsonify({"msg": "still no born"}), 400
        else:
            return jsonify(response_body), 200

    if request.method == 'DELETE':
        result = jackson_family.delete_member(id)
        response_body = {
            "msg": "member deleted successfully",
            "actual_members": result,
            "done": True
        }
        return jsonify(response_body), 200


@app.route('/member', methods=['POST'])
def handle_add_member():

    member_id = request.json.get('id', jackson_family._generateId())
    first_name = request.json.get('first_name', None)
    age = request.json.get('age', None)
    lucky_numbers = request.json.get('lucky_numbers', None)

    new_member = {
                "id": member_id,
                "first_name": first_name,
                "last_name": "Jackson",
                "age": age,
                "lucky_numbers": lucky_numbers
    }

    if member_id is not None or first_name is not None or age is not None or lucky_numbers is not None:
        result = jackson_family.add_member(new_member)
        return jsonify(result), 200
    else:
        return jsonify('please insert valid data'), 400
    



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)