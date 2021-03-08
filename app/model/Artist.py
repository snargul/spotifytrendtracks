class Artist:
    artist_id = None
    full_name = None

    def __init__(self, artist_id=None, full_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.artist_id = artist_id
        self.full_name = full_name
