from marshmallow import Schema, fields

class PlanetsFavoriteSchema(Schema):
    id=fields.Int(dump_only=True)
    user_id=fields.Int(required=True)
    planet_id=fields.Int(required=True)
    createdAt=fields.DateTime(dump_only=True)
    updatedAt=fields.DateTime(dump_only=True)
