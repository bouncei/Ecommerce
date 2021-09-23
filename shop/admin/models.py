# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from shop import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True, nullable=False)
    username = db.Column(db.String(100),unique=True, nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    profile = db.Column(db.String(100), unique=False, nullable=False, default='profile.jpg')

    def __repr__(self):
        return '<User %r>' % self.username

# class Products(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.String(100), nullable=False)
#     pass

# class Customers(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     pass


# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     pass

# db.create_all()
