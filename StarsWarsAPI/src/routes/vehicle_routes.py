from flask import Blueprint, request

from flask_jwt_extended import jwt_required,get_jwt_identity
from controllers.vehicle_controller import get_all, get_user
vehicle_routes = Blueprint("vehicle", __name__)

@vehicle_routes.route('/', methods=['GET'])
@jwt_required()
def users():
    if request.method == 'GET':
        return get_all()


@vehicle_routes.route('/<int:id>', methods=['GET'])
def user(id):
    if request.method == 'GET':
        return get_user(id)
 
