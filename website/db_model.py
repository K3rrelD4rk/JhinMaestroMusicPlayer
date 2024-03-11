from . import db
import json
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import UserMixin, login_required, current_user
from sqlalchemy.sql import func

views = Blueprint('views', __name__)


class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    Name = db.Column(db.String(150))
    Surname = db.Column(db.String(150))
    Username = db.Column(db.String(150) )
    email = db.Column(db.String(150), secondary_key=True)
    password = db.Column(db.String(150))
    playlists = db.relationship('Playlists')
    down_songs = db.relationship('Offline_songs')
    
class Playlists(db.Model):
    id = db.Column(db.integer, primary_key=True)
    pl_name = db.Column(db.String(150))
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    
class Offline_songs(db.Model):
    id = db.Column(db.integer, primary_key =True)
    Song_name = db.Column(db.String(150))
    
