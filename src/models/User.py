from config import app, db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column('id', db.Integer, primary_key=True)
    name          = db.Column('name', db.String(100))
    email         = db.Column('email', db.String(50))
    password      = db.Column('password', db.String(100))
    created_at    = db.Column('created_at', db.DateTime, default=datetime.utcnow)
    updated_at    = db.Column('updated_at', db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, password):
        self.id = self.id
        self.name = name
        self.email = email
        self.password = password
        self.created_at = self.created_at
        self.updated_at = self.updated_at


    def __repr__(self):
        return '{"id": %d, "name":"%s", "email":"%s", "password":"%s", "created_at": "%s", "updated_at":"%s"}' % (self.id, self.name, self.email, self.password, self.created_at, self.updated_at)