from marshmallow import Schema, fields, validate


class EmployeeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=80))
    surname = fields.Str(required=True, validate=validate.Length(min=1, max=70))
    email = fields.Email(required=True, validate=validate.Length(min=1, max=100))
    position = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    salary = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    hire_date = fields.Date(required=True, dump_only=True)


class EmployeeUpdateSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1, max=80))
    surname = fields.Str(validate=validate.Length(min=1, max=70))
    email = fields.Email(validate=validate.Length(max=100))
    position = fields.Str(validate=validate.Length(min=1, max=50))
    salary = fields.Decimal(places=2, validate=validate.Range(min=0))
