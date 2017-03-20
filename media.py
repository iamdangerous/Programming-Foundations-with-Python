class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self,title,movie_storyline,poster_image,trailer_youtube_url):
        self.title = title;
        self.movie_storyline = movie_storyline;
        self.poster_image_url = poster_image;
        self.trailer_youtube_url = trailer_youtube_url;
