from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # hashed_password = generate_password_hash(password=password, method='pbkdf2:sha256', salt_length=8).split("$")[2]
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        print(f"Hashed password: {hashed_password}")

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. Please login.', 'error')
            return redirect(url_for('login'))

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('secrets', name=new_user.name))

    return render_template("register.html", logged_in=current_user.is_authenticated)


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = User.query.filter_by(email=email).first()
#
#         # print(f"Entered email: {email}")
#         # print(f"Entered password: {password}")
#         # print(f"User found: {user}")
#         # print(f"Hashed password: {user.password}")
#
#         if user and check_password_hash(user.password, password):
#             print("User successfully authenticated.")
#             login_user(user)
#             print(f"Current user: {current_user}")
#             return redirect(url_for('secrets', name=user.name))
#
#         print("Invalid email or password.")
#         flash('Invalid email or password. Please try again.', 'error')
#
#         # User not found, handle appropriately
#         if not user:
#             flash('Email not registered. Please sign up.', 'error')
#
#     return render_template("login.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user is None:
            flash('Email does not exist. Please check your email or register.', 'error')
            return redirect(url_for('login'))

        if user and not check_password_hash(user.password, password):
            flash('Incorrect password. Please try again.', 'error')
            return redirect(url_for('login'))

        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            login_user(user)
            return redirect(url_for('secrets', name=user.name))

    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', filename='cheat_sheet.pdf', as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
