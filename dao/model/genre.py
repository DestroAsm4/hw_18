from setup_db import db
from marshmallow import Schema, fields

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()