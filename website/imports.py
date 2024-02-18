import random
import string
from dotenv import load_dotenv
import requests
import json
from io import StringIO
import os
import hashlib
load_dotenv()

s = requests.session()
def verify(client_id, redirect_uri):
    code_verify = ' '.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = 128))
    code_verify = hashlib.sha256(code_verify.encode())
    code_verify = code_verify.digest()
    scope = "user-read-private user-read-email"
    auth_url = "https://accounts.spotify.com/authorize"
    h = {"response_type" : 'code'}
    g = s.get(auth_url, headers = h ,auth =(client_id), data = { "scope" : scope, "code_challenge" : code_verify, "code_challenge_method" : 'S256'})
    c = json.loads(g.content.decode('utf-8'))

def token(client_id, client_secret, redirect_uri):
    url = "https://accounts.spotify.com/api/token"
    h = {"Content-Type": "application/x-www-form-urlencoded"}
    d = {'grant_type': 'client_credentials'}
    p = s.post(url, headers=h, data=d, auth=(client_id, client_secret))
    a = json.loads(p.content.decode("utf-8"))
    return a

