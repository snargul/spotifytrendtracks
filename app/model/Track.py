class Track:
    """Track represents a piece of music on Spotify"""
    artist = None
    track = None
    album_image_url = None
    release_date = None

    def __init__(self, artis_name=None, track_name=None, image=None, date=None, *args, **kwargs):
        """
        :param track_id (int): Spotify track id
        :param name (str): Track name
        :param artist (obj): Artist who created the track
        :param album (obj): Album of track
        """
        super().__init__(*args, **kwargs)
        self.artist = artis_name
        self.track = track_name
        self.album_image_url = image
        self.release_date = date

    def __str__(self):
        return "{artist: " + self.artist + \
               ", track: " + self.track + \
               ", album_image_url: " + self.album_image_url + \
               ", release_date: " + self.release_date + "}"
