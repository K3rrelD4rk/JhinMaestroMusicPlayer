from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from os import path
load_dotenv()

db = SQLAlchemy()
DB_NAME = "database.db"

ME_URL = 'https://api.spotify.com/v1/me'

# Start 'er up
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'hdfdsfgdufdgfidsufgdsuig'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .imports import imports
    from .views import views
    
    app.register_blueprint(imports, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    
    from .management import User
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
    
    
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        engine = create
        print('Created Database!')