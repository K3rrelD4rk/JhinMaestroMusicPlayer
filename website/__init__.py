from APIs import  auth
from imports import token
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
)
import os
load_dotenv()

ME_URL = 'https://api.spotify.com/v1/me'

# Start 'er up
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('/website/sito/index.html')

def main():
    code = os.getenv("CODE")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")
    token_client = token(client_id, client_secret,redirect_uri,code)
    Token = token_client["access_token"]
    print(Token)
    Refresh_token = token_client["refresh_token"]
    print(Refresh_token)
    