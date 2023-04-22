from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource
from dotenv import load_dotenv
from os import environ
from marshmallow import post_load, fields, ValidationError

load_dotenv()

# Create App instance
app = Flask(__name__)

# Add DB URI from .env
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')

# Registering App w/ Services
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app)
Migrate(app, db)

# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Float, nullable = False)


# Schemas
class ProductSchema(ma.Schema):
    id = fields.Integer(primary_key = True)
    name = fields.String(required = True)
    description = fields.String(required = True)
    price = fields.Float(required = True)

    class Metaa:
        fields = ("id","name","description","price")

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)


# Resources
class ProductListResources(Resource):
    def get(self):
        return "Hello World"


# Routes
api.add_resource(ProductListResources,'api/products/')