from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

def connect_to_db(app, db_name):
    """Connect to the db"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(os.environ[
    'DB_USERNAME'], os.environ['DB_PASSWORD'],os.environ['DB_SERVER'], db_name)
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    date_updated = db.Column(db.DateTime, server_default=db.func.now(),
        server_onupdate=db.func.now())
    users = db.relationship('User', backref='team')
    total_points = db.relationship('Point', secondary='user')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    date_updated = db.Column(db.DateTime, server_default=db.func.now(),
        server_onupdate=db.func.now())

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reason = db.Column(db.Text)
    date_created = db.Column(db.DateTime, server_default=db.func.now())

if __name__ == '__main__':
    app = Flask(__name__)
    connect_to_db(app, 'teampoints')
    db.create_all()
