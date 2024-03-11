import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
load_dotenv()

if __name__ == '__main__':
    #Auth Spotify API
    client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("CLIENT_ID"),
                                                          client_secret=os.getenv("SECRET_CLIENT"))
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    #Serves variables to flask webserver
    app = Flask(__name__)
    
    @app.route('/artistname', methods=['GET'])
    def searchTrack():
        artistImgURL = 'None'
        artistTrackURL = 'None'
        artistURI = 'None'
        textboxInput = request.args.get('artistName')
        
        searchInput = textboxInput
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        results = spotify.search(q='artist' + searchInput, type='artist')
        items = results['artist']['items']
        if len(items) > 0:
            artist = items[0]
            artistImgURL = artist['images'][0]['url']
            artistURI = artist['uri']
            artistTrackURL = artist
            results_uri = spotify.artist_top_tracks(artistURI)
            
            searchresultsOut = []
            for track in results_uri['tracks'][:10]:
                searchresultsOut.append([track['name']])
                artistTrackURL = track['prev_url']
        #----------------------------------------------------------------
        return format(artistTrackURL)
        #return render_template('index.html', img=artistTrackImgURL, mp3=artistTrackURL, searchresults=searchresultsOut)
    
    @app.route('/songsearch', methods=['GET'])
    def searchArtist():
        artistsearchgetinout = request.args.get('artistsearch')
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        results = spotify.search(q='track:' + artistsearchgetinout, type='track')
    
        #search tracks
        searchresultsOut = {}
        for track in results['tracks']['items'][:1]:
            trackName = track['name']
            trackMP3 = track['preview_url']
            trackImg = track['album']['images'][0]['url']
            searchresultsOut = '{"trackName": "' + trackName + '", "trackMP3": "' + trackMP3 + '", "trackImg": "' + trackImg + '"}'
    
        return format(searchresultsOut)

    app.run(host="::1", port=26656, debug=True)