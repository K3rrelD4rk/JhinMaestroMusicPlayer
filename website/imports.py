import random
import requests
import json
from io import StringIO
import hashlib

def verify(client_id, redirect_uri):
    code_verify = hashlib.sha256.digest(random.Random(128))
    scope = "user-read-private user-read-email"
    auth_url = "https://accounts.spotify.com/authorize"
    s = requests.session()
    g = s.get(auth_url, auth =(client_id), scope = scope, response_type= 'code', code_challenge = code_verify, code_challenge_method = 'S256')


def token(client_id, client_secret, redirect_uri):
    url = "https://accounts.spotify.com/api/token"
    s = requests.session()
    h = {"Content-Type": "application/x-www-form-urlencoded"}
    d = {'grant_type': 'client_credentials'}
    p = s.post(url, headers=h, data=d, auth=(client_id, client_secret))
    a = json.loads(p.content.decode("utf-8"))
    token = a["access_token"]
    return token


def get_profile(userid, email):