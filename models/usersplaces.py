from testapp.db import db

users_places_table = db.Table('users_places', db.Model.metadata,
    db.Column('uid', db.Integer, db.ForeignKey('users.id')),
    db.Column('pid', db.Integer, db.ForeignKey('places.id'))
)