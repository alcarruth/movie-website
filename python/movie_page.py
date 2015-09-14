#!/usr/bin/python

from sys import path
movie_root = path[0]
template_dir = movie_root + '/src/templates/'
image_dir =  movie_root + '/src/templates/'

from movie_util import get_youtube_id, data_url, read_file

# At an abstract level, a movie page is just a collection of movies, 
# formated so a web browser can render a user friendly interface
# efficiently.
#
# So we have just two classes here: Movie_Tile and Movie_Page.
# Each has an html template stored in an external file which is loaded
# as a static member.  The filenames for the templates correspond
# to the classnames for which they are intended.  (see below.)
# Each class has a method to_html() which will render an instance
# using the template.

class Movie_Tile:

    # Load the template for the movie tile as a static, 'class', attribute
    template = read_file(template_dir + 'movie_tile_template.html')

    def __init__(self, movie):
        self.title = movie['title']
        self.image_path = movie['image']
        self.trailer_url = movie['trailer']
        self.description = movie['description']

    # Feature Alert !!
    # image_src() can inline jpeg images just by calling it
    # with img_online=True
    #
    def image_src(self, img_inline=False):
        if img_inline:
            return data_url(movie_root + '/dist/' + self.image_path)
        else:
            return self.image_path

    # Return the html for this movie tile.
    def to_html(self, img_inline=False):
        tile_html = self.template.format(
            movie_title = self.title,
            image_src = self.image_src(img_inline),
            youtube_trailer_id = get_youtube_id(self.trailer_url),
            description = self.description
            )
        return tile_html

class Movie_Page:

    # Load the template for the movie page as a static, 'class', attribute
    template = read_file(template_dir + 'movie_page_template.html')

    def __init__(self, movies, img_inline=False):

        # in Python you can map a constructor - kinda cool
        self.movie_tiles = map(Movie_Tile, movies)

        # self.img_inline is a boolean flag which is passed to a tile's
        # to_html() method below
        self.img_inline = img_inline

    def set_img_inline(self, b):
        self.img_inline = b

    def to_html(self):
        # Return the html for this page.
        tiles_section = map(lambda(tile): tile.to_html(self.img_inline), self.movie_tiles)
        return self.template.format(movie_tiles = str.join('\n', tiles_section))
