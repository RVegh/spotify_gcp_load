import os
import spotipy
import spotipy.util as util
import settings

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify()

client_credentials_manager = SpotifyClientCredentials(client_id=settings.SPOTIPY_CLIENT_ID, client_secret=settings.SPOTIPY_CLIENT_SECRET,)

def main():
    spotify_connection = util.prompt_for_user_token(username=settings.username,
                                            scope=settings.scope,
                                            client_id=settings.SPOTIPY_CLIENT_ID,
                                            client_secret=settings.SPOTIPY_CLIENT_SECRET,
                                            redirect_uri=settings.redirect_uri)
    
    token = client_credentials_manager.get_access_token()
    spotify_token = spotipy.Spotify(auth=token)

       
if __name__ == '__main__':
   main()
