#creating database models for users and notes
from . import db #importing from current package "website" the db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #all notes must belong to a user:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #must pass a valid id of an existing user to this column when a note
    #object is made^^

class User(db.Model, UserMixin):
    #define all columns we want stored in the table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #creating a relationship with the Note table

