from flask import Flask
from . import api, db_model
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db_model = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db_model.init_app(app)
    
    from .db_model import views
    
    app.register_blueprint(views, url_prefix='/')
    
    
    from .db_model import User, Playlists, Offline_songs
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_auth = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db_model.create_all(app=app)
        print('Created Database!')