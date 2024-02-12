import random
from dotenv import load_dotenv
import requests
import json
from io import StringIO
import os
import hashlib
load_dotenv()

s = requests.session()
def verify(client_id, redirect_uri):
    code_verify = hashlib.sha256.digest(random.Random(128))
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
    token = a["access_token"]
    return token


#def get_profile(userid, email):
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("SECRET_CLIENT")

#code_verify = hashlib.sha256.digest(random.Random(128))
code_verify = hashlib.sha256(hashlib.digest(random.Random(128)))
scope = "user-read-private user-read-email"
auth_url = "https://accounts.spotify.com/authorize"
h = {"response_type" : 'code'}
d = { "scope" : scope, "code_challenge" : code_verify, "code_challenge_method" : 'S256'}
s = requests.session()
g = s.get(auth_url, headers = h , data = d)
c = json.loads(g.content.decode('utf-8'))
print(c)