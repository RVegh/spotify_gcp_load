import os
import spotipy
import spotipy.util as util
import settings

from spotipy.oauth2 import SpotifyClientCredentials

def spotify_connection():
    spotify = util.prompt_for_user_token(username=settings.username,
                                            scope=settings.scope,
                                            client_id=settings.SPOTIPY_CLIENT_ID,
                                            client_secret=settings.SPOTIPY_CLIENT_SECRET,
                                            redirect_uri=settings.redirect_uri)

spotify_connection()
'''
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
'''

