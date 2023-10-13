from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

ADMIN_EMAIL = 'admin@email.com'
ADMIN_PASSWORD = '12345678'
class LoginForm(FlaskForm):
    email = StringField(label='Email: ', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password: ', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = 'nubcoder@420'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.email.data == ADMIN_EMAIL and login_form.password.data == ADMIN_PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
