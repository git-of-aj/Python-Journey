from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# capture variable given in url like /ananay so name = 'ananay'
@app.route("/<name>")
def hi_name(name):
    return f'Hi {name}'

# note :
'''
jinja auto does but otherwise be sure to deal with untrsuted data = <name>
use :
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
'''

#___________________________________________________
'''
http://127.0.0.1:5000/ananay --> WORKS...

STRANGE!!
http://127.0.0.1:5000/ananay/ --> gives error : 
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.

'''

#______________________________________________
'''
YOU CAN CONVERT THE VARIABLE TYPE SUPPLIED IN URL, <STRING> == DEFAULT
https://flask.palletsprojects.com/en/2.2.x/quickstart/#variable-rules
'''
