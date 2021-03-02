from app.service import JsonService
from app.service.SpotifyApiService import SpotifyApiService
from app.service.JsonService import JsonService
from app.data.constants import genre_json_file_path
from app.data import messages


class AppService(object):
    genre_json_file_path = None
    genre = None
    artist_name = None
    track_list = None

    def __init__(self, genre=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genre_json_file_path = genre_json_file_path
        self.genre = genre

    def setGenre(self, genre):
        self.genre = genre

    def listTopTracks(self, genre):
        json_service = JsonService(genre_json_file_path, genre)
        selected_artist = json_service.getRandomValue()
        sp_api = SpotifyApiService(selected_artist)
        artist_info = sp_api.searchArtist()
        artist_name = artist_info['name']
        track_list = sp_api.readTopTracks()
        return self.top_list_obj(artist_name, track_list)

    @staticmethod
    def top_list_obj(artist_name, track_list):
        top_list = []
        for track in track_list:
            track_info = {
                'artist': artist_name,
                'track': track['name'],
                'album_image_url': track['album']['images'][0]['url'],
                'release_date': track['album']['release_date']
            }
            top_list.append(track_info)
        return top_list

    @staticmethod
    def getGenreTypeList():
        json_service = JsonService(genre_json_file_path)
        return json_service.getJsonKeys()

    def checkInputOK(self, genre_input):
        if genre_input is None:
            return False, messages.input_empty
        genre = str(genre_input).lower()
        genre_list = self.getGenreTypeList()
        if genre not in genre_list:
            return False, messages.input_not_match
        else:
            return True, genre
