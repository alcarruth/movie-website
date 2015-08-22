#!/usr/bin/python -i

from fresh_tomatoes import *

# todo: 
movie_html_template = """
<li class="movie">
<a href="%(trailer_url)s" target="trailer">
<img src="%(image_url)s" alt="%(image_url)s">
</a>
<p> %(title)s</p>
"""
# todo: html5 has images with captions?

class Movie:

    def __init__(self, title, image_url, trailer_url):
        self.title = title
        self.image_url = image_url
        self.trailer_url = trailer_url

    def gen_html(self):
        return movie_html_template % self.__dict__

#if __name__ == '__main__':
#    generate_movies_page([], "movie_trailers.html")


movie = Movie("Test Movie", "http://trailer.mp4", "http://image.png")

print movie.gen_html()


