from flask import current_app, jsonify
from models import Planets
from schema import PlanetsSchema
from utils import db
from sqlalchemy.orm import joinedload




def get_all():
    try: 
        query= db.select(Planets).order_by(Planets.id)
        planets = db.session.execute(query).scalars().all()
        if len(planets) == 0:
            return jsonify({"message": "No hay usuarios"}), 404
        planet_schema = PlanetsSchema(many=True)
        data = planet_schema.dump(planets)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener los planetas", "error": str(error)})    
def get_user(id):
    try:
        query= db.select(Planets).where(Planets.id == id)
        planet = db.session.execute(query).scalars().all()
        if len(planet) == 0:
            return jsonify({"message": "Planeta no encontrado"}), 404
        planet_schema = PlanetsSchema(many=True)
        data = planet_schema.dump(planet)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el planeta", "error": str(error)})