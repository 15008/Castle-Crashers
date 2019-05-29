from flask import render_template, redirect, url_for
from app import app, db
from app.models import Movie
from app.models import Actor


@app.route('/')
def home():
    return render_template('home.html', page_title="Home Page")

@app.route('/all_movies')
def all_movies():
	movies = Movie.query.all()
	return render_template('all_movies.html',page_title="Movie Names", movies=movies)

@app.route("/movie/<id>")
def movie(id):
    movie = Movie.query.filter_by(id = id).first()
    return render_template('movie_details.html', page_title="Details", movie=movie)
