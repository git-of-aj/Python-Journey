------------------------------------------------------------------------
# INSTALLATION OF VENV (AND FLASK)
# VENV == YOUR ISOLATED ISLAND IN THE SEA OF PYTHON
# APP INSTALLED IN THIS VENV ARE SEPERATED FROM REST OF PYTHON IN YOUR MACHINE

#create dir
mkdir this_is_venv
#create a vnev with name 
python3 -m venv this_is_venv
# activate 
this_is_venv\scripts\activate             or ./this_is_venv/bin/activate  --> for linux

#install flask
pip install flask
----------------------------------------------------------------------
# import Flask class from Flask module
# Flask function - WSGI application.
# WSGI: 
from flask import Flask

# __name__ represents presen file
# flask(__name__):
# let the Flask function knows where to look for resources such as templates and static files.
app = Flask(__name__)

#route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

#----------------------------------------------
# flask command or python -m flask like this: 
# flask run 
# flask run --host=0.0.0.0 --> hosts app over your private ip 

'''
* Running on http://127.0.0.1:5000
 * Running on http://192.168.29.123:5000
 But accepts request from all internal networks
'''
#------------------------------------------------------
# Other commands

'''
flask run --port 5001 
'''

# NOTES
'''
1. give name app.py only else vaery very errors
'''
