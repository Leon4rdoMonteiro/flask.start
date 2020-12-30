from flask import Blueprint, request, jsonify

from users.service import UserService

users = Blueprint('users', __name__)
userService = UserService()

@users.route('/users', methods=['POST'])
def create():
    response = userService.create(request.json)
    return jsonify(response), response['status_code']


@users.route('/users/<user_id>', methods=['GET'])
def show(user_id): 
    response = userService.show(user_id)
    return jsonify(response), response['status_code']
            

@users.route('/users', methods=['GET'])
def index():
    response = userService.index()
    return jsonify(response), response['status_code']


@users.route('/users/<user_id>', methods=['PUT'])
def update(user_id):
    response = userService.update(user_id, request.json)
    return jsonify(response), response['status_code']


@users.route('/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    response = userService.delete(user_id)
    return jsonify(response), response['status_code']