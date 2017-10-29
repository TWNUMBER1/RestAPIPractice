from testapp.db import db
from usersplaces import users_places_table
from store import StoreModel
import json
import flask

from sqlalchemy import *

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    delete_tag = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)

    # foreign relationship
    places = db.relationship("StoreModel", secondary=users_places_table, backref=db.backref('users', lazy=True))


    def __init__(self, user):
        self.name = user['name']
        self.delete_tag = user['delete_tag']
        self.created_date = user['created_date']

    def __repr__(self):
        return '<User %r>' % (self.name)

    def json(self):
        return {'name': self.name, 'uuid': self.id}

    @classmethod
    def find_by_id(cls, id):
        flask.current_app.logger.info('find_by_id id = %s ', id)
        ret = cls.query.filter_by(id=id).first()
        return ret

    @classmethod
    def get_all_users(cls):
        flask.current_app.logger.info('getting all users %s ', cls.query.first().__dict__)
        users = cls.query.all()
        return users

    def get_all_places(self):
        return self.places

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()