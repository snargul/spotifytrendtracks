from app.service.SpotifyApiService import SpotifyApiService
from app.service.JsonService import JsonService
from app.model.Artist import Artist
from app.model.Album import Album
from app.model.Track import Track


class AppService(object):
    json_service = None
    spotify_api_service = None

    def __init__(self, json_service: JsonService, spotify_api_service: SpotifyApiService,
                 input_empty_msg, input_not_match_msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json_service = json_service
        self.spotify_api_service = spotify_api_service
        self.input_empty_msg = input_empty_msg
        self.input_not_match_msg = input_not_match_msg

    def listTopTracks(self, genre):
        selected_artist = self.json_service.getRandomValueByKey(genre)
        artist_info = self.spotify_api_service.searchArtist(selected_artist)
        artist = Artist(artist_info['id'], artist_info['name'])
        track_list = self.spotify_api_service.readTopTracks(artist.artist_id)
        obj_list = self.createList(artist, track_list)
        return obj_list

    @staticmethod
    def createList(artist, track_list):
        result_list = []
        for each in track_list:
            album = Album(each['album']['images'][0]['url'], each['album']['release_date'])
            track = Track(artist.full_name, each['name'], album.image_url, album.release_date)
            result_list.append(track)
        return result_list

    def getGenreTypeList(self):
        return self.json_service.getJsonKeys()

    def checkInputOK(self, genre_input):
        if genre_input is None:
            return False, self.input_empty_msg
        genre = str(genre_input).lower()
        genre_list = self.getGenreTypeList()
        if genre not in genre_list:
            return False, self.input_not_match_msg
        else:
            return True, genre
