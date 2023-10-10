from flask import Flask, render_template, request
from post import Post
import requests as r
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = 'EMAIL'
MY_PASSWORD = 'PASSWORD'

posts = r.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html", all_posts=post_objects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

@app.route('/form-entry', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        send_email_notification(name, email, phone, message)

        return render_template('form-entry.html', success_message='Succesfully sent your message!')

def send_email_notification(name, email, phone, message):

    email_message = f"Message sent from your Blog\n\n" \
                f"From {name}:\n" \
                f"Message: {message}\n" \
                f"Email: {email}\n" \
                f"Phone: {phone}\n\n" \

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        msg = MIMEText(email_message, 'plain', 'utf-8')
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        msg['Subject'] = f"Message sent from your Blog!"

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=msg.as_string(),
        )
    print("Notification Sent")
    print(name)
    print(email)
    print(phone)
    print(message)



if __name__ == "__main__":
    app.run(debug=True)
