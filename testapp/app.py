from flask import Flask
from yelpUtil import yelp
from models.store import StoreModel
# from db import db
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)
# db.init_app(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.route("/")
def hello():
    return yelp.getNearbyList()

@app.route("/nearbylist", methods=['GET'])
def getNearbyList():
    # GET yelp restaurant list
    return "Not implemented yet\n"

@app.route("/mylist", methods=['GET'])
def getMyList():
    # Get user favorite list
    return "Not implemented yet\n"

@app.route("/store/<string:restaurant>", methods=['POST'])
def storeRestaurant(restaurant):
    # Store user favorite restaurant
    return "Not implemented yet\n"

