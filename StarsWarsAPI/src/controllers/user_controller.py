from flask import current_app, jsonify
from models import User
from schema import UserSchema,UserSchemaExtend
from utils import db
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash

from sqlalchemy.orm import joinedload




def get_all():
    try: 
        query= db.select(User).order_by(User.id)
        users = db.session.execute(query).scalars().all()
        if len(users) == 0:
            return jsonify({"message": "No hay usuarios"}), 404
        user_schema = UserSchema(many=True)
        data = user_schema.dump(users)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})    
def get_user(id):
    try:
        query= db.select(User).where(User.id == id)
        user = db.session.execute(query).scalars().all()
        if len(user) == 0:
            return jsonify({"message": "Usuario no encontrado"}), 404
        user_schema = UserSchema(many=True)
        data = user_schema.dump(user)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})

def get_allfavorites():
    try: 
        query= db.select(User).order_by(User.id)
        users = db.session.execute(query).scalars().all()
        if len(users) == 0:
            return jsonify({"message": "No hay usuarios"}), 404
        user_schema = UserSchemaExtend(many=True)
        data = user_schema.dump(users)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})    
def get_userfavorites(id):
    try:
        query= db.select(User).where(User.id == id)
        user = db.session.execute(query).scalars().all()
        if len(user) == 0:
            return jsonify({"message": "Usuario no encontrado"}), 404
        user_schema = UserSchemaExtend(many=True)
        data = user_schema.dump(user)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})
    
def create_user(request):
    try:
        user_schema = UserSchema()
        query= db.select(User).where(User.email == request.json['email'])
        user = db.session.execute(query).scalars().first()
        if user:
            return jsonify({"message": "El usuario ya existe"}), 400
        user=request.json
        user_data = user_schema.load(user)
        hashed_password = generate_password_hash(user_data['password']).decode('utf-8')
        user=User(**user_data)
        user.password=hashed_password
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario creado exitosamente","data":user_schema.dump(user)}), 201
    except Exception as error:
        return jsonify({"message": "Error al crear el usuario", "error": str(error)}),400
    
def login (request):
    try:
        user_schema = UserSchema()
        user_data = request.json
        query= db.select(User).where(User.email == user_data['email'])
        user = db.session.execute(query).scalars().first()
        if not user:
            return jsonify({"message": "El usuario no existe"}), 400
        if check_password_hash(user.password,user_data['password']) :
            payload={}
            payload={"id":user.id,"name":user.name,"email":user.email}
            access_token=create_access_token(identity=payload)
            return jsonify({"message": "Usuario logeado exitosamente","token":access_token,"user": user_schema.dump(user)}), 200
        else:
            return jsonify({"message": "Contraseña incorrecta"}), 400
    except Exception as error:
        return jsonify({"message": "Error al logear el usuario", "error": str(error)}),400