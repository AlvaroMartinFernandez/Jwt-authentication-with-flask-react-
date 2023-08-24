from flask import Blueprint, request
from flask_jwt_extended import jwt_required,get_jwt_identity

from controllers.planet_controller import get_all, get_user
planet_routes = Blueprint("planet", __name__)

@planet_routes.route('/', methods=['GET'])
@jwt_required()
def users():
    if request.method == 'GET':
        return get_all()


@planet_routes.route('/<int:id>', methods=['GET'])
def user(id):
    if request.method == 'GET':
        return get_user(id)
 
