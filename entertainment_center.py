import media
import fresh_tomatoes
toy_story  = media.Movie("Toy Story","Just a toy story","http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg","https://www.youtube.com/watch?v=_CH6Os4tfyg");

#print(toy_story.title);
print(media.Movie.__doc__)
movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
