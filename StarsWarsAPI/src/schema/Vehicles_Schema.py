from marshmallow import Schema, fields

class VehiclesSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    url=fields.Str(required=True)
    model=fields.Str(required=True)
    vehicle_class=fields.Str(required=True)
    manufacturer=fields.Str(required=True)
    cost_in_credits=fields.Str(required=True)
    length=fields.Str(required=True)
    crew=fields.Str(required=True)
    passengers=fields.Str(required=True)
    max_atmosphering_speed=fields.Str(required=True)
    cargo_capacity=fields.Str(required=True)
    consumables=fields.Str(required=True)
    createdAt=fields.DateTime(dump_only=True)
    updatedAt=fields.DateTime(dump_only=True)
    