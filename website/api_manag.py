import json
import requests
from dotenv import load_dotenv
import os, base64
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
import webbrowser
load_dotenv()

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
client_id = os.getenv("CLIENT_ID")
secret_client = os.getenv("SECRET_CLIENT")
redirect_uri = os.getenv("REDIRECT_URI")
def auth():
    auth_code_headers = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "user-library-read"
    }
    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_code_headers))
    with urllib.request.urlopen(redirect_uri) as response:
        data = response.read()
        print (data)
    auth_code = requests.get(AUTH_URL, auth_code_headers)
    auth_header = base64.urlsafe_b64encode((client_id + ':' + secret_client).encode())
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % auth_header
    }
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
       'redirect_uri': redirect_uri,
       'client_id': client_id,
       'client_secret': secret_client
    }
    access_token_request = requests.post(TOKEN_URL, data=payload, headers=headers)
    access_token_response = access_token_request.json()
    print (access_token_response)
    #access_token = access_token_response['access_token']
    
