from datetime import datetime

from blogger.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_image = db.Column(db.String(120), nullable=False, default='user.jpg')
    password = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now())

