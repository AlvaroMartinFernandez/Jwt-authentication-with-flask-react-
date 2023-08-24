import os

from flask import Flask,jsonify
from utils import db
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler


# Import models
from models.User import User
from models.Peoples import Peoples
from models.Planets import Planets
from models.Vehicles import Vehicles
from models.Peoples_Favorite import PeoplesFavorite
from models.Planets_Favorite import PlanetsFavorite
from models.Vehicles_Favorite import VehiclesFavorite



# Import routes
from routes.api import api



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    db.init_app(app)
    jwt = JWTManager(app)
    bcrypt = Bcrypt(app)
    cors =CORS(app)

    with app.app_context():
        try:
            db.create_all()
            total_records = db.session.query(User).count()
            print(f"La conexión a la base de datos fue exitosa. Total de registros en la tabla 'User': {total_records}")
        except Exception as e:
            print("Error al conectarse a la base de datos:", str(e))

   
            
    return app, bcrypt, jwt,cors

app, bcrypt, jwt, cors = create_app()

app.register_blueprint(api, url_prefix='/')   

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)


if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('HOST') or '127.0.0.1', port = os.getenv('PORT') or 5000)
