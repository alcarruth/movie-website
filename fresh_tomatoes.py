import webbrowser
import os
import re
import string

def read_text_file(file_name):
    text_file = open(file_name, 'r')
    text_str = string.join(text_file.readlines())
    text_file.close()
    return text_str

def write_text_file(text_str, file_name):
    text_file = open(file_name, 'w')
    text_file.write(text_str)
    text_file.close()

def get_youtube_id(youtube_url):
    # Extract the youtube ID from the url
    match = re.search( r'(?<=v=)[^&#]+', youtube_url)
    match = match or re.search( r'(?<=be/)[^&#]+', youtube_url)
    return match.group(0) if match else None

def create_movie_tiles(movies):
    # The HTML content for this section of the page
    template = read_text_file('movie_tile_template.html')
    movie_tiles = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        movie_tiles += template.format(
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = get_youtube_id(movie.trailer_youtube_url),
            storyline = movie.storyline
        )
    return movie_tiles

def create_movies_page(movies):
    # Load the html template file
    template = read_text_file('fresh_tomatoes_template.html')
    movie_tiles = create_movie_tiles(movies)
    # Replace the movie tiles placeholder generated content
    movies_page = template.format(movie_tiles = movie_tiles)
    return movies_page

def open_movies_page(movies):

    file_name = 'fresh_tomatoes.html'
    movies_page = create_movies_page(movies)
    write_text_file(movies_page, file_name)

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(file_name)
    webbrowser.open('file://' + url, new=2)
