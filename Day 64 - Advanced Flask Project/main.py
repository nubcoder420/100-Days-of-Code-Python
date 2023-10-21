from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired
import requests


MOVIE_DB_API_KEY = 'e5d814059aafe5a4bdbc1d7d0e572e23'
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

#------ Create Database -----#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#----- Create Table -----#
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

# with app.app_context():
#     db.create_all()
#
#     #----- Create Movie Example -----#
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()

class RateMovieForm(FlaskForm):
    rating = FloatField("Rating", validators=[DataRequired()])
    review = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Search')

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    form = RateMovieForm(obj=movie)

    if request.method == "POST" and form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form, movie=movie)

@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovieForm()

    if form.validate_on_submit():
        title = form.title.data
        response = requests.get(
            url=MOVIE_DB_SEARCH_URL,
            params={
                "api_key": MOVIE_DB_API_KEY,
                "query": title,
                }
        )
        data = response.json()['results']
        return render_template('select.html', options=data)

    return render_template('add.html', form=form)

@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(
            url=movie_api_url,
            params={
                "api_key": MOVIE_DB_API_KEY,
                "language": "en-US",
            }
        )
        data = response.json()

        new_movie = Movie(
            title=data['title'],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )

        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("rate_movie", id=new_movie.id))

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


if __name__ == '__main__':
    app.run(debug=True)
