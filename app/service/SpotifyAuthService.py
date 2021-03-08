import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from app.exception.AuthorizationException import AuthorizationException


class SpotifyAuthService(object):
    clint_id = None
    clint_secret = None
    spotipy = None

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clint_id = client_id
        self.clint_secret = client_secret
        self.authorize()

    def authorize(self):
        if self.clint_id is None or self.clint_secret is None or self.clint_id is '' or self.clint_secret is '':
            raise AuthorizationException()
        try:
            self.spotipy = spotipy.Spotify(
                auth_manager=SpotifyClientCredentials(client_id=self.clint_id, client_secret=self.clint_secret))
        except Exception:
            raise AuthorizationException()

    def getSpotify(self):
        return self.spotipy
