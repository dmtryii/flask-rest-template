
from flask import request, jsonify
from app.services import users_services 
from app.controllers.users import bp


@bp.route('/', methods=['GET'])
def get_users():
    users = users_services.get_all()
    json_users= list(map(lambda x: x.to_dict(), users))
    return jsonify({'users': json_users}), 200


@bp.route('/', methods=['POST'])
def create_contact():    
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


# @app.route('/contact/<int:id>', methods=['PATCH'])
# def update_contact(id):
#     contact = Contact.query.get(id)
    
#     if not contact:
#         return jsonify({'message': 'User not found'}), 404
    
#     data = request.json
#     contact.first_name = data.get('firstName', contact.first_name)
#     contact.last_name = data.get('lastName', contact.last_name)
#     contact.email = data.get('email', contact.email)
    
#     db.session.commit()
    
#     json_contact = contact.to_json()
#     return jsonify({'contact': json_contact}), 200
    

# @app.route('/contact/<int:id>', methods=['DELETE'])
# def delete_contact(id):
#     contact = Contact.query.get(id)
    
#     if not contact:
#         return jsonify({'message': 'User not found'}), 404
    
#     db.session.delete(contact)
#     db.session.commit()
    
#     return jsonify({'message': 'User deleted'}), 204
