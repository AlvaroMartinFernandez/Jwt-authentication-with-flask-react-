from utils import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    createdAt = db.Column(db.DateTime, server_default=db.func.now())
    updatedAt = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    peoples_favorites = db.relationship('Peoples', back_populates='user', secondary= 'peoplesfavorites' ,lazy=True)
    vehicles_favorites = db.relationship('Vehicles', back_populates='user', secondary= 'vehiclesfavorites' ,lazy=True)
    planets_favorites = db.relationship('Planets', back_populates='user', secondary= 'planetsfavorites' ,lazy=True)
