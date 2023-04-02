## Jinja template docs ---> https://jinja.palletsprojects.com/en/3.1.x/templates/#filters


```
JINJA TEMPLATE BASICS:

{% ... %} for Statements ==> LIKE {% for i in range(10) %} {%endfor %}

{{ ... }} for Expressions to print to the template output ====> like {{variable}}

{# ... #} for Comments not included in the template output
```
# filter = some methods supported in  python like -->string.capitalize = {{ string | capitalize }} 
  # docs https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters

  # test :
  {% if loop.index is divisibleby 3 %}
{% if loop.index is divisibleby(3) %}
  
# template inheritance = you want same features, methods acroos all pages like a navigation bar, header, footer then create a base template, import these settings from base
# to child template 

  # --------------------------------------------------------------------------------------------------------------------------------------
  
  # app.py file to have template inheritance
  
  from flask import Flask, url_for , render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html",link=url_for('child'))

@app.route("/child")
def child():
    return render_template("child.html")

@app.route("/<name>")
def hi(name):
    letters_list = list(name)
    length = len(letters_list)
    letters_dict = {'letter1': letters_list[0],'letter2': letters_list[1],
                    'start-2-end': f"there start 2 end {letters_list[0:]}"}
    # return render_template("filename under template folder", variables)
    return render_template("index.html", name = name, alphabets = letters_list, 
                           key_value = letters_dict,len = length)

with app.test_request_context():
  # this prints output to test in the terminal
    print(url_for('child'))

if __name__ == "__main__":
    app.run(debug=True)
