# Display static Contents

## How to render HTML, CSS -> Static files??

- simple no connection, varibles need from flask python files ---> **create a folder named static** --> keep all static files there


`url_for('static', filename='style.css')`
- render_template() ---->
All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.

# create folder in the same directory --> use static 

```py
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    link = url_for("timer_greets", name="/<name>")
    return f"<h1> Welcome to Timer - Python</h1> <a href='{link}'>visit here to Get a Hi 👋</a> <h2> append your name after URL like: /name see magic <h2>"

@app.route("/<name>")
def timer_greets(name):
    static_files = url_for('static',filename = 'test.html')
    return f"Hi {name}, It's Timer <a href = '{static_files}' > HTML Page !! </a>"


```
**Observation so far:**
- Tried changing folder name to test  and also giving path to folder nothing worked :
 ```py
 url_for('test',filename = 'index.html')
 
 # Point 2
 url_for('../static',filename = 'index.html')
```
## Dynamic Pages -- Templates 
**A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. **

```py
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def hello(name='Ananay'):
    static_files = url_for('static', filename='test.html')

    template_url = url_for('temp', name=name)
    return f"Hi {name}, It's Timer <a href='{static_files}'>This is HTML Page !!</a> visit <a href='{template_url}'>for dynamic python page</a>"

@app.route("/<name>")
def temp(name):
    return render_template('index.html.jinja', name=name)

if __name__ == '__main__':
    app.run(debug=True)

```
