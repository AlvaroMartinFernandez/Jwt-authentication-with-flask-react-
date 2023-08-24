from flask import Blueprint, request

# from flask_jwt_extended import jwt_required,get_jwt_identity
from controllers.favorite_controller import createpeoplefav,deletepeoplefav,createplanetsfav,deleteplanetsfav,createvehiclesfav,deletevehiclesfav
favorite_routes = Blueprint("favorite", __name__)

@favorite_routes.route('/people/<int:people_id>', methods=['POST','DELETE'])
def peoplesfav(people_id):
    if request.method == 'POST':
        return createpeoplefav(people_id)
    if request.method == 'DELETE':
        return deletepeoplefav(people_id)


@favorite_routes.route('/planet/<int:planet_id>', methods=['POST','DELETE'])
def planetsfav(planet_id):
    if request.method == 'POST':
        return createplanetsfav(planet_id)
    if request.method == 'DELETE':
        return deleteplanetsfav(planet_id)
    

@favorite_routes.route('/vehicle/<int:vehicle_id>', methods=['POST','DELETE'])
def vehiclesfav(vehicle_id):
    if request.method == 'POST':
        return createvehiclesfav(vehicle_id)
    if request.method == 'DELETE':
        return deletevehiclesfav(vehicle_id)

