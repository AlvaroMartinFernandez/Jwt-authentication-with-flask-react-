from marshmallow import  fields, validate, ValidationError
from schema import UserSchema,PeoplesSchema,VehiclesSchema,PlanetsSchema

class UserSchemaExtend(UserSchema):
  peoples_favorites= fields.List(fields.Nested(PeoplesSchema))
  vehicles_favorites= fields.List(fields.Nested(VehiclesSchema))
  planets_favorites= fields.List(fields.Nested(PlanetsSchema))
