from marshmallow import Schema, fields

class PlanetsSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    url=fields.Str(required=True)
    diameter=fields.Str(required=True)
    rotation_period=fields.Str(required=True)
    orbital_period=fields.Str(required=True)
    gravity=fields.Str(required=True)
    population=fields.Str(required=True)
    climate=fields.Str(required=True)
    terrain=fields.Str(required=True)
    surface_water=fields.Str(required=True)
    createdAt=fields.DateTime(dump_only=True)
    updatedAt=fields.DateTime(dump_only=True)
    