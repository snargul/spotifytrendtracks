from app.service.SpotifyAuthService import SpotifyAuthService
from app.data.constants import popular_track_list_range
from app.data import messages


class SpotifyApiService(object):
    spotify = None
    artist_name = None
    artist_id = None

    def __init__(self, artist_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spotify = SpotifyAuthService().getSpotify()
        self.artist_name = artist_name

    def searchArtist(self):
        results = self.spotify.search(q='artist:' + self.artist_name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            self.artist_id = artist['id']
            return artist
        else:
            raise Exception(messages.artist_not_found)

    def readTopTracks(self):
        artist_uri = f"spotify:artist:{self.artist_id}"
        results = self.spotify.artist_top_tracks(artist_uri)
        if results is None or results['tracks'] is None:
            raise Exception(messages.track_not_found)
        print(popular_track_list_range)
        return results['tracks'][:popular_track_list_range]
