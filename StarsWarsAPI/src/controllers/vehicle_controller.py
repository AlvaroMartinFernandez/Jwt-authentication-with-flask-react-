from flask import current_app, jsonify
from models import Vehicles
from schema import VehiclesSchema
from utils import db
from sqlalchemy.orm import joinedload




def get_all():
    try: 
        query = db.session.query(Vehicles).order_by(Vehicles.id)
        vehicles = db.session.execute(query).scalars().all()
        if len(vehicles) == 0:
            return jsonify({"message": "No hay vehiculos"}), 404
        vehicle_schema = VehiclesSchema(many=True)
        data = vehicle_schema.dump(vehicles)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el vehiculos", "error": str(error)})    
def get_user(id):
    try:
        query = db.session.query(Vehicles).where(Vehicles.id == id)
        vehicle = db.session.execute(query).scalars().all()
        if len(vehicle) == 0:
            return jsonify({"message": "Vehiculo no encontrado"}), 404
        vehicle_schema = VehiclesSchema(many=True)
        data = vehicle_schema.dump(vehicle)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el vehiculo", "error": str(error)})