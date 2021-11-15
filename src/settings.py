import os

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

username = '12182510882'
scope ='user-read-recently-played'
redirect_uri = 'http://localhost:7777/callback'
