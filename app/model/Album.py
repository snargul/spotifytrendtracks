class Album:
    album_id = None
    image_url = None
    release_date = None

    def __init__(self, image_url, release_date):
        self.release_date = release_date
        self.image_url = image_url
