from marshmallow import Schema, fields


class Error(Schema):
    message = fields.String(required=True,)


class Spacecraft(Schema):
    description = fields.String()
    id = fields.Raw(required=True,)

    name = fields.String(required=True,)
    type = fields.String(required=True,)


class SpacecraftId(Schema):
    pass
