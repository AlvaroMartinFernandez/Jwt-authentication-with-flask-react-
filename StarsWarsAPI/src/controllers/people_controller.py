from flask import current_app, jsonify
from models import Peoples
from schema import PeoplesSchema
from utils import db
from sqlalchemy.orm import joinedload




def get_all():
    try: 
        query= db.select(Peoples).order_by(Peoples.id)
        peoples = db.session.execute(query).scalars().all()
        if len(peoples) == 0:
            return jsonify({"message": "No hay usuarios"}), 404
        people_schema =PeoplesSchema(many=True)
        data = people_schema.dump(peoples)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})    
def get_user(id):
    try:
        query= db.select(Peoples).where(Peoples.id == id)
        people = db.session.execute(query).scalars().all()
        if len(people) == 0:
            return jsonify({"message": "Usuario no encontrado"}), 404
        people_schema = PeoplesSchema(many=True)
        data = people_schema.dump(people)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})