import os

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

username = '12182510882'
scope ='user-read-recently-played'
redirect_uri = 'http://localhost:7777/callback'

'''
SPOTIPY_CLIENT_ID = '92df6eee95ad4f92a4777420819d05db'
SPOTIPY_CLIENT_SECRET = '1aa4401e43a14973bec0863f24a2dd3b'
'''