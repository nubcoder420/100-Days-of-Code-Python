from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Ensure an application context is active
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books = Book.query.all()
    if not books:
        return render_template('index.html', message="Library is empty.")
    return render_template('index.html', all_books=books)

@app.route("/add", methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        rating = request.form.get('rating')

        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')

@app.route('/edit_rating/<int:book_id>', methods=['GET', 'POST'])
def edit_rating(book_id):
    book = Book.query.get(book_id)

    if request.method == 'POST':
        new_rating = request.form.get('new_rating')
        book.rating = float(new_rating)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit_rating.html', book=book)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)

    if book:
        db.session.delete(book)
        db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)