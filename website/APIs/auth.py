#!/usr/bin/env python
import requests
import json
from io import StringIO
s = requests.session()
url = "https://accounts.spotify.com/api/token"
CLIENT_ID = "be5f21610a7347d08a5fc9c621b7f141"
SECRET_CLIENT = "109ba1df69804424a5ff820522549cfa"
h = {"Content-Type" : "application/x-www-form-urlencoded"}
d = {'grant_type' : 'client_credentials' }
p = s.post( url , headers = h , data = d, auth = (CLIENT_ID , SECRET_CLIENT))
a = json.loads(p.content.decode("utf-8"))
token = a["access_token"]
