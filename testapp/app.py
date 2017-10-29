from flask import Flask, request, abort, jsonify
from db import db
from flask_sqlalchemy import SQLAlchemy
from models.users import UserModel
from models.store import StoreModel
import json

import datetime

app = Flask(__name__)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)
db.init_app(app)


@app.route("/")
def hello():
    return "hello!"

@app.route("/users", methods=['GET'])
def getAllUsers():
    app.logger.info('Entering getAllUsers method')
    users = UserModel.get_all_users()
    ret = []
    for user in users:
        if user is not None:
            ret.append(user.json())

    return json.dumps(ret), 200

@app.route("/user/<string:id>", methods=['GET'])
def getUser(id):
    app.logger.info('Entering getAllUsers method')
    user = UserModel.find_by_id(id)
    return (json.dumps(user.json()), 200)if user is not None else ("", 200)


@app.route("/places", methods=['GET'])
def getAllPlaces():
    app.logger.info('Entering getAllPlaces method')
    places = StoreModel.get_all_places()
    ret = []
    for place in places:
        if place is not None:
            ret.append(place.json())
    return json.dumps(ret), 200

@app.route("/place/<int:id>", methods=['GET'])
def getUserPlaces(id):
    app.logger.info('Entering getUserPlaces method')
    user = UserModel.find_by_id(id)
    if user is None:
        return ""
    places = user.get_all_places()
    ret = []
    for place in places:
        if place is not None:
            ret.append(place.json())
    return json.dumps(ret)

@app.route('/user', methods=['POST'])
def createUser():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'name': request.json['name'],
        'delete_tag': 0,
        'created_date': datetime.datetime.now()
    }
    user = UserModel(user)
    user.save_to_db()
    return jsonify({'user': user.name}), 201

@app.route('/place', methods=['POST'])
def createPlace():
    if not request.json or \
       not 'name' in request.json or \
       not 'gid' in request.json or \
       not 'address' in request.json or \
       not 'yelpurl' in request.json or \
       not 'userID' in request.json:
        abort(400)

    user = UserModel.find_by_id(request.json['userID'])
    if user is None:
        return "User not found", 400

    place = {
        'name': request.json['name'],
        'gid': request.json['gid'],
        'address': request.json['address'],
        'yelpurl': request.json['yelpurl'],
        'delete_tag': 0,
        'created_date': datetime.datetime.now()
    }
    place = StoreModel(place)
    place.users.append(user)
    place.save_to_db()
    return jsonify({'place': place.name}), 201
