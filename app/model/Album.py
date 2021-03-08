class Album:
    album_id = None
    image_url = None
    release_date = None

    def __init__(self, image_url=None, release_date=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.release_date = release_date
        self.image_url = image_url
