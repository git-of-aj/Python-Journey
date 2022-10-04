- and, or, and not) are used to compare Boolean values
```py
name = 'Carol'
   age = 3000
   if name == 'Alice':
       print('Hi, Alice.')
   elif age < 12:
       print('You are not Alice, kiddo.')
➊ elif age > 100: # --> this BLOCK PRINTS --> IT'S TRUE + APPEARS FIRST
       print('You are not Alice, grannie.') # ORDER MATTERS IN ELIF
   elif age > 2000:
       print('Unlike you, Alice is not an undead, immortal vampire.')
````
