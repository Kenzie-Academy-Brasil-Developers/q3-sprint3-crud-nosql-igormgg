from app import routes
from flask import Flask
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['kenzie']

def create_app():

    app = Flask(__name__, static_folder=None)
    app.config['JSON_SORT_KEYS'] = False
    routes.init_app(app)

    return app