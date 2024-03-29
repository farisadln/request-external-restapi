from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Gaji(db.Model):
    __tablename__ = 'gaji'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    gaji = db.Column(db.String(150), nullable=False)


    def __init__(self, name,gaji):
        self.name = name
        self.gaji = gaji

class GajiSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    gaji = fields.String(required=False)