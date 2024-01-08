#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#import requests

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
LOGIN_URL = "https://accounts.spotify.com/api/login"
CLIENT_ID = "be5f21610a7347d08a5fc9c621b7f141"
SECRET_CLIENT = "109ba1df69804424a5ff820522549cfa"
REDIRECT_URI = "https://localhost:3000"
results = sp.current_user_saved_tracks()

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artist'][0]['name'], " - ", track['name'])