#----- Flask Installation -----#
"""
#Create Virtual Environment
mkdir myproject
cd myproject
py -3 -m venv .venv

#Activate the Environment
.venv\Scripts\activate

#Install Flask
pip install Flask
"""


#----- Flask Quickstart -----#
#hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

#----- Run Flask Server -----#
#use terminal
'''
python -m flask --app hello.py run
'''

#or
if __name__ == "__main__":
    app.run()


#----- Python Decorators -----#
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #do something before
        function()
        function()
        #do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print('Hello')

@delay_decorator
def say_bye():
    print('Bye')

def say_greeting():
    print('Greetings!')



