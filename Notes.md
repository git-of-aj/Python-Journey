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

## If vs While 

```py
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

# Here is the code with a while statement:

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
```
![](https://automatetheboringstuff.com/2e/images/000072.jpg)

**While - Loop**
![](https://automatetheboringstuff.com/2e/images/000112.jpg)

## while true : Continue: Break 💔
```py
 while True:
      print('Who are you?')
      name = input()
    ➊ if name != 'Joe':
        ➋ continue
       print('Hello, Joe. What is the password? (It is a fish.)')
    ➌ password = input()
       if password == 'swordfish':
        ➍ break
➎ print('Access granted.')    

# If the user enters any name besides Joe ➊, the continue statement ➋ causes the program execution to jump back to the start of the loop
```
## for 
block of code only a certain number of times

> continue and break statements only inside while and for loops. If you try to use these statements elsewhere, Python will give you an error.

If you accidentally name one of your programs, say, random.py, and use an import random statement in another program, your program would import your random.py file instead of Python’s random module. This can lead to errors such as AttributeError: module 'random' has no attribute 'randint', since your random.py doesn’t have the functions that the real random module has.

- example, from random import *.

With this form of import statement, calls to functions in random will not need the random. prefix. However, using the full name makes for more readable code, so it is better to use the import random form of the statement.

- def hello(name):
    ➋ print('Hello, ' + name)

➌ hello('Alice')
   hello('Bob')

[Define, Call, Pass, Argument, Parameter](https://automatetheboringstuff.com/2e/chapter3/#Define,%20Call,%20Pass,%20Argument,%20Parameter)
