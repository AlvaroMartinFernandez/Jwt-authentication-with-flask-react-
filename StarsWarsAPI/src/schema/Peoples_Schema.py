from marshmallow import Schema, fields

class PeoplesSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    url=fields.Str(required=True)
    height=fields.Str(required=True)
    mass=fields.Str(required=True)
    hair_color=fields.Str(required=True)
    skin_color=fields.Str(required=True)
    eye_color=fields.Str(required=True)
    birth_year=fields.Str(required=True)
    gender=fields.Str(required=True)
    homeworld=fields.Str(required=True)
    createdAt=fields.DateTime(dump_only=True)
    updatedAt=fields.DateTime(dump_only=True)
    