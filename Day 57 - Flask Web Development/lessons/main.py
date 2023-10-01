from flask import Flask, render_template
from datetime import datetime
import requests

current_year = datetime.utcnow().year

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html", copyright_year=current_year)

@app.route("/guess/<name>")
def guess(name):
    name = name.title()
    # print(name)

    r = requests.get(url=f"https://api.agify.io/?name={name}")
    age = r.json().get("age")

    r = requests.get(url=f"https://api.genderize.io/?name={name}")
    gender = r.json().get("gender")

    # print(age)
    # print(gender)
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

