from utils import db

class Peoples(db.Model):
    __tablename__ = 'peoples'
    # Here we define db.Columns for the table person
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    height=db.Column(db.String(250), nullable=False)
    mass=db.Column(db.String(250), nullable=False)
    hair_color= db.Column(db.String(250), nullable=False)
    skin_color=db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    homeworld=db.Column(db.String(250), nullable=False)
    createdAt = db.Column(db.DateTime, server_default=db.func.now())
    updatedAt = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user=db.relationship('User', back_populates='peoples_favorites', secondary= 'peoplesfavorites' ,lazy=True)
