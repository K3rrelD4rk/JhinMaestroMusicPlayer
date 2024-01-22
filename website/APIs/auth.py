#!/usr/bin/env python
import token
from urllib.parse import urlencode
import requests
from dotenv import load_dotenv
import os
import base64
import webbrowser
load_dotenv()

code = "AQDBW9ZIIjjAJbRQ6BRkVsXKJvK1w3KdsbUXwo2OMShwo9YV5CNH9Q9MroFYog54bcYCFmKNR8hwAubKR_8EqQm2zUkjt26WL35wZNdoBr1hT2YmFG_YHm8Em8E1qfr3HpAQbtbXL4I7KZ-UZbnTtiZvKJjt4hH9KcgJlWLVdpWtCaRD5xUXmqTT5QmN"
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("SECRET_CLIENT")
redirect_url = os.getenv("REDIRECT_URL")
LOGIN_URL = "https://accounts.spotify.com/api/login"

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_url,
    "scope": "user-library-read"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_url
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)