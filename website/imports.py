import requests
import json
from io import StringIO

def token(client_id, client_secret,redirect_uri):
    url = "https://accounts.spotify.com/api/token"
    s = requests.session()
    h = {"Content-Type" : "application/x-www-form-urlencoded"}
    d = {'grant_type' : 'client_credentials' }
    p = s.post( url , headers = h , data = d, auth = (client_id , client_secret))
    a = json.loads(p.content.decode("utf-8"))
    token = a["access_token"]
    return token()
