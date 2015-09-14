#!/usr/bin/env python

import sys
movie_root = sys.path[0]
python_dir = movie_root + '/python'
dist_dir = movie_root + '/dist'
sys.path.append(python_dir)

import webbrowser
from os import path

# movie_db is our input data file
# movie_db.movies is a list of python dictionaries
# with the following keys:
#   title: title string
#   image: relative path to a jpeg image
#   trailer: youtube url string
#   description: multiline string
#
from movie_db import movies
from movie_page import Movie_Page
from movie_util import read_file, write_file

def gen_page(page, page_file, img_inline=False):
    page.set_img_inline(img_inline)
    write_file(page.to_html(), page_file)

def view_page(page_file):
    # open the output file in the browser (in a new tab, if possible)
    url = path.abspath(page_file)
    webbrowser.open('file://' + url)

def test_page(page, page_file, img_inline=False):
    out_file = dist_dir + '/' + page_file
    gen_page(page, out_file, img_inline)
    view_page(out_file)

if __name__=='__main__':
    page = Movie_Page(movies)
    test_page(page, 'fresh_tomatoes.html')
    test_page(page, 'fresh_tomatoes_inline.html', True)




