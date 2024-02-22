import random
import string
from urllib.parse import urlencode
import base64
import webbrowser
from dotenv import load_dotenv
from flask import Blueprint
import requests
import json
from io import StringIO
import os
import hashlib
load_dotenv()

imports = Blueprint('imports', __name__)

s = requests.session()

def verify(client_id, redirect_uri):
    code_verify = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = 16))
    code_verify = hashlib.sha256(code_verify.encode())
    code_verify = code_verify.digest()
    scope = "user-read-private user-read-email"
    auth_url = "https://accounts.spotify.com/authorize?"
    h = {"response_type" : 'code' , "redirect_uri" : redirect_uri, "scope" : scope, "client_id" : client_id, "code_challenge" : code_verify, "code_challenge_method" : 'S256'}
    g = s.get(auth_url, headers = h)
    c = json.loads(g.content.decode('utf-8'))
    return c

def tokens(client_id, client_secret, redirect_uri, code):
    url = "https://accounts.spotify.com/api/token"
    h = {"Content-Type": "application/x-www-form-urlencoded" , "redirect_uri" : redirect_uri}
    d = {'grant_type': 'client_credentials', "code" : code, "redirect_uri": redirect_uri}
    p = s.post(url, headers=h, data=d, auth=(client_id, client_secret))
    a = json.loads(p.content.decode("utf-8"))
    return a

