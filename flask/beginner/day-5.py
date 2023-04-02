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
