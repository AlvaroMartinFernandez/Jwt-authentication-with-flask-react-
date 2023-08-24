from flask import current_app, jsonify
from models import Peoples, User, Planets, Vehicles, PeoplesFavorite, PlanetsFavorite, VehiclesFavorite
from schema import PlanetsFavoriteSchema, PeoplesFavoriteSchema, VehiclesFavoriteSchema
from utils import db
from sqlalchemy.orm import joinedload

#COMO NO TENEMOS LOGIN NO PODEMOS USAR EL PAYLOAD DEL JWT PARA TENER UN USUARIO ACTUAL POR QUE QUE PODEMOS COMO USUARIO ACTUAL EL USUARIO CON LA ID =1

def createpeoplefav(id):
    try:
        schema_people= PeoplesFavoriteSchema()
        user_id = 1 #get_jwt_identity()
        query= db.select(PeoplesFavorite).where(PeoplesFavorite.user_id == user_id, PeoplesFavorite.people_id == id)
        peoplefav = db.session.execute(query).first()
        if peoplefav:
            return jsonify({"msg": "People already in favorites"}), 400
        query= db.select(User).where(User.id == user_id)
        user = db.session.execute(query).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        query= db.select(Peoples).where(Peoples.id == id)
        people = db.session.execute(query).first()
        if not people:
            return jsonify({"msg": "People not found"}), 404
        result={}
        result['user_id']=user_id
        result['people_id']=id
        peoplefavdata = schema_people.load(result)  
        peoplefav= PeoplesFavorite(**peoplefavdata)
        db.session.add(peoplefav)
        db.session.commit()
        return jsonify({"msg": "People added to favorites"}), 200
    except Exception as error:
        current_app.logger.error(error)
        return jsonify({"msg": "Internal server error"}), 500
def deletepeoplefav(id):
    try:
        user_id = 1 #get_jwt_identity()
        peoplefav = db.session.query(PeoplesFavorite).filter_by(user_id=user_id, people_id=id).first()
        if not peoplefav:
            return jsonify({"msg": "Persona no encontrada"}), 404
        db.session.delete(peoplefav)
        db.session.commit()
        return jsonify({"msg": "People removed from favorites"}), 200
    except Exception as error:
        current_app.logger.error(error)
        return jsonify({"msg": "Internal server error"}), 500
def createplanetsfav(id):
    try:
        schema_planet = PlanetsFavoriteSchema()
        user_id = 1 #get_jwt_identity()
        query= db.select(PlanetsFavorite).where(PlanetsFavorite.user_id == user_id, PlanetsFavorite.planet_id == id)
        planetfav = db.session.execute(query).first()
        if planetfav:
            return jsonify({"msg": "People already in favorites"}), 400
        query= db.select(User).where(User.id == user_id)
        user = db.session.execute(query).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        query= db.select(Planets).where(Planets.id == id)
        planet = db.session.execute(query).first()
        if not planet:
            return jsonify({"msg": "People not found"}), 404
        result={}
        result['user_id']=user_id
        result['planet_id']=id
        planetfavdata = schema_planet.load(result)
        planetfav= PlanetsFavorite(**planetfavdata)
        db.session.add(planetfav)
        db.session.commit()
        return jsonify({"msg": "Planet add from favorites"}), 200
    except Exception as error:
        current_app.logger.error(error)
        return jsonify({"msg": "Internal server error"}), 500
def deleteplanetsfav(id):
    try:
        schema_planet = PlanetsFavoriteSchema()
        user_id = 1 #get_jwt_identity()
        planetfav = db.session.query(PlanetsFavorite).filter_by(user_id=user_id, planet_id=id).first()
        if not planetfav:
            return jsonify({"msg": "Planet not found"}), 404
        db.session.delete(planetfav)
        db.session.commit()
        return jsonify({"msg": "Planet removed from favorites"}), 200
    except Exception as error:
        current_app.logger.error(error)
        return jsonify({"msg": "Internal server error"}), 500
def createvehiclesfav(id):
    try:
        schema_vehicle = VehiclesFavoriteSchema()
        user_id = 1 #get_jwt_identity()
        query= db.select(VehiclesFavorite).where(VehiclesFavorite.user_id == user_id, VehiclesFavorite.vehicle_id == id)
        vehiclefav = db.session.execute(query).first()
        if vehiclefav:
            return jsonify({"msg": "People already in favorites"}), 400
        query= db.select(User).where(User.id == user_id)
        user = db.session.execute(query).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404
        vehicle = Vehicles.query.get(id)
        if not vehicle:
            return jsonify({"msg": "Vehicle not found"}), 404
        result={}
        result['user_id']=user_id
        result['vehicle_id']=id
        vehiclefavdata = schema_vehicle.load(result)
        vehiclefav= VehiclesFavorite(**vehiclefavdata)
        db.session.add(vehiclefav)
        db.session.commit()
        return jsonify({"msg": "Vechicle add from favorites"}), 200
    except Exception as error:
        current_app.logger.error(error)
        return jsonify({"msg": "Internal server error"}), 500
def deletevehiclesfav(id):
    try:
        schema_vehicle = VehiclesFavoriteSchema()
        user_id = 1 #get_jwt_identity()
        vehiclefav = db.session.query(VehiclesFavorite).filter_by(user_id=user_id, vehicle_id=id).first()
        if not vehiclefav:
            return jsonify({"msg": "Vehicle not found"}), 404
        db.session.delete(vehiclefav)
        db.session.commit()
        return jsonify({"msg": "Vehicle removed from favorites"}), 200
    except Exception as error:
        current_app.logger.error(error)
        return jsonify({"msg": "Internal server error"}), 500