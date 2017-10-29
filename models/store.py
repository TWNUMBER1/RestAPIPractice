from testapp.db import db
import json
import flask

class StoreModel(db.Model):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    gid = db.Column(db.Integer)
    address = db.Column(db.String(200))
    yelpurl = db.Column(db.String(200))
    delete_tag = db.Column(db.Integer)
    count = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)

    def __init__(self, place):
        self.name = place['name']
        self.gid = place['gid']
        self.address = place['address']
        self.yelpurl = place['yelpurl']
        self.delete_tag = place['delete_tag']
        self.created_date = place['created_date']
        self.count = 0

    def json(self):
        return {'name': self.name, 'address': self.address}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_places(cls):
        flask.current_app.logger.info('getting all places')
        users = cls.query.all()
        return users

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()