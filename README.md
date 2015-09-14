

# Movie Trailer Website

## Quick Start

> `$ git clone git@github.com:alcarruth/fullstack-p1-movie-website.git`
>
> `$ cd fullstack-p1-movie-website`
>
> `$ ./run_me.py`

## Description 

This is a simple application written in python which generates a
pair of movie trailer webpages:

 * `fresh_tomatoes.html`
 * `fresh_tomatoes_inline.html`

The two are identical except that for the second one the images
are inlined in the `<img>` tags.  The base64 encoding of the images
is done on the fly by the app.

An attempt at responsive design has been made so that resizing the
brwoser window does not destroy the aesthetics of the page.

## Directory Structure

 * `python/movie_db.py`
 * `python/movie_page.py`
 * `python/movie_util.py`
 * `src/images/`
 * `src/scripts/`
 * `src/style/`
 * `src/templages/`
 * `dist/images/`
 * `dist/scripts/`
 * `dist/style/`

Running the executable python script `run_me.py` in the project root directory 
results in the two fresh_tomatoes html files being written into the dist 
directory and opened in browser tabs.  If you only want one of them, you 
can easily comment out the other in `run_me.py`.

