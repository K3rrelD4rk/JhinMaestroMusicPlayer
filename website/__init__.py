from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from APIs import auth

db = SQLAlchemy()
DB_NAME = "offline.db"


def create_app():
    app.cre

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database')