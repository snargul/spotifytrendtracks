from app.model.Artist import Artist
from app.model.Album import Album


class Track:
    """Track represents a piece of music on Spotify"""
    track_id = None
    name = None
    artist = None
    album = None

    def __init__(self, track_id, name, artist_id, artist_name, album_image_url, album_release_date):
        """
        :param track_id (int): Spotify track id
        :param name (str): Track name
        :param artist (obj): Artist who created the track
        :param album (obj): Album of track
        """
        self.track_id = track_id
        self.name = name
        self.artist = Artist(artist_id, artist_name)
        self.album = Album(album_image_url, album_release_date)

    def __str__(self):
        return f"{self.name} by {self.artist.full_name}, released at {self.album.release_date}"
