
from flask import request, jsonify
from app.services import users_services 
from app.controllers.users import bp


@bp.route('/', methods=['GET'])
def get_users():
    users = users_services.get_all()
    json_users= list(map(lambda x: x.to_dict(), users))
    return jsonify({'users': json_users}), 200


@bp.route('/', methods=['POST'])
def create_user():    
    new_user = users_services.create(
        username=request.json.get('username'),
        first_name=request.json.get('firstName'),
        last_name=request.json.get('lastName'),
        password=request.json.get('password'),
        email=request.json.get('email'),
        gender=request.json.get('gender'),
        birthday=request.json.get('birthday')
    )
    
    return jsonify({'user': new_user.to_dict()}), 201
