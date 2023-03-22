'''
If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.
url_for() is a Flask method that generates a URL for a given endpoint.
url_for == ahref in HTML (somewhat simiar)
url_for (name-of-python-function-to-answer-this,argument1,argument2,so on)
more in docs: https://flask.palletsprojects.com/en/2.2.x/quickstart/#url-building
'''

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1> Hey There </h1>'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
'''
Results of the print statements respectively:

/
/login
/login?next=%2F
/user/John%20Doe

Notice how it handles passed agruments as variables, stores unspecified varibles like /next as query string in the url..

'''

DIY:
    
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    link = url_for("timer_greets", name="/<name>")
    return f"<h1> Welcome to Timer - Python</h1> <a href='{link}'>visit here to Get a Hi 👋</a> <h2> append your name after URL like: /name see magic <h2>"

@app.route("/<name>")
def timer_greets(name):
    return f"Hi {name}, It's Timer "

