from marshmallow import Schema, fields

class PeoplesFavoriteSchema(Schema):
    id=fields.Int()
    user_id=fields.Int(required=True)
    people_id=fields.Int(required=True)
    createdAt=fields.DateTime(dump_only=True)
    updatedAt=fields.DateTime(dump_only=True)