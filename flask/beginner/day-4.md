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
    # here name = name means ==> variable-specified-inside-template = value-to-be-taken
    return f"Hi {name}, It's Timer <a href='{static_files}'>This is HTML Page !!</a> visit <a href='{template_url}'>for dynamic python page</a>"

@app.route("/<name>")
def temp(name):
    return render_template('index.html.jinja', name=name)

if __name__ == '__main__':
    app.run(debug=True)

```

## Debugging 

it looks for files under template directory unless specified otherwise 
```py
from flask import Flask, url_for , render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1> Hey There </h1>'

@app.route('/timer')
def timer():
    return render_template("./static/test.html")
# RAISE ERROR COZ IT'S UNDER A DIFFERENT DIRECTORY CALLED STATIC

if __name__ == "__main__" :
    app.run(debug=True)

```

## using all data types in html

```py
from flask import Flask, url_for , render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1> Hey There </h1>'

@app.route("/<name>")
def hi(name):
    letters_list = list(name)
    letters_dict = {'letter1': letters_list[0],'letter2': letters_list[1],
                    'start-2-end': f"there start 2 end {letters_list[0:]}"}
    # return render_template("filename under template folder", variables)
    return render_template("index.html", name = name, alphabets = letters_list, key_value = letters_dict)

if __name__ == "__main__":
    app.run(debug=True)

```

```html
// THIS IS HTML FILE UNDER TEMPLATE folder
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> Hello {{name}} 😊 </h1>
    <h2> There is lists from python :</h2>
    <p> {{alphabets}}</p>
    <h2> There is key-value from python :</h2>
    <p> {{key_value}}</p>
    <h3> here is a specific key-value name : {{key_value['start-2-end']}}</h3>
    
</body>
</html>
```
## Observation;
- In your HTML template using python functions like : len(list) doesn't works --> `<h2>TOtal Letters in your name: {{len(alphabets)}}</h2>` gives error  --> jinja2.exceptions.UndefinedError: 'len' is undefined
