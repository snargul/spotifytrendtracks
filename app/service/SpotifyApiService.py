from app.service import SpotifyAuthService


class SpotifyApiService(object):
    spotify = None
    list_range = None
    artist_not_found_msg = ''
    track_not_found_msg = ''

    def __init__(self, spotify_auth_service: SpotifyAuthService, list_range, artist_not_found_msg, track_not_found_msg,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spotify = spotify_auth_service.getSpotify()
        self.list_range = list_range
        self.artist_not_found_msg = artist_not_found_msg
        self.track_not_found_msg = track_not_found_msg

    def searchArtist(self, artist_name):
        results = self.spotify.search(q='artist:' + artist_name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            return items[0]
        else:
            raise Exception(self.artist_not_found_msg)

    def readTopTracks(self, artist_id):
        artist_uri = f"spotify:artist:{artist_id}"
        results = self.spotify.artist_top_tracks(artist_uri)
        if results is None or results['tracks'] is None:
            raise Exception(self.track_not_found_msg)
        print(self.list_range)
        return results['tracks'][:self.list_range]
