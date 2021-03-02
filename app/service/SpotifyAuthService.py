import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from app.exception.AuthorizationException import AuthorizationException


class SpotifyAuthService(object):
    clint_id = None
    clint_secret = None
    spotipy = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clint_id = os.getenv('SP_CLIENT_ID')
        self.clint_secret = os.getenv('SP_CLIENT_SECRET')
        self.authorize()

    def authorize(self):
        if self.clint_id is None or self.clint_secret is None:
            raise AuthorizationException()
        self.spotipy = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id=self.clint_id, client_secret=self.clint_secret))

    def getSpotify(self):
        return self.spotipy
