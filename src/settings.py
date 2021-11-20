import os

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

username = '12182510882'
scope ='user-library-read'
authorization_url = 'https://accounts.spotify.com/authorize'
redirect_uri = 'http://localhost:7777/callback'

