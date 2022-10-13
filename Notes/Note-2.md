> Lists and tuples can contain multiple values, which makes writing programs that handle large amounts of data easier.
- The Python sequence data types include lists, strings, range objects returned by range(), and tuples
- all above give sequencing, indexing etc

## Lists 
list is a value that contains multiple values in an ordered sequence
```py
spam = ['cat', 'bat', 'rat', 'elephant']
   >>> spam
   ['cat', 'bat', 'rat', 'elephant']
``` 
![](https://automatetheboringstuff.com/2e/images/000090.jpg)
**Indexes can be only integer values, not floats**

Helps in handling : 
- large amount of data 
- create hierarchy [list can contain other lists]

```py
# creates a variable spam with 2 lists
# list 0 = [cat, bat]
# list 1 = [10,20..]
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1] # 0 indicates which list --> the 1 indicates which item in 
# seleted list
'bat'
>>> spam[1][4]
50
```
- Lists values can be changed(varname / new-value = list[index], del list[index], replicated list*number, concatenate [L1,l2] L= list
- [intelligently use list with for loop]()

### Multiple Variable Assignment 

```py
>>> cat = ['fat', 'gray', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]

# you could type this line of code:

>>> cat = ['fat', 'gray', 'loud']
>>> size, color, disposition = cat
```

**NOTE : The number of variables and the length of the list must be exactly equal, or Python will give you a ValueError:**

## Enumerate Function, Random choice, random shuffle
- enumerate() will return two values: the index of the item in the list, and the item in the list itself

```py
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
>>> for index, item in enumerate(supplies):
...     print('Index ' + str(index) + ' in supplies is: ' + item)

Augmented Assignment of Variables

spam = 'Hello,'
>>> spam += ' world!'
>>> spam
'Hello world!'
>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
```

### Python Tricks
- Line Continuation in python (\)
```py
# to make lists look readable you can also provide 
# spaces -- python ignores and just check 
# square brackets 
spam = ['apples',
    'oranges',
                    'bananas',
'cats']
print(spam)
```

Strings used like : Lists 
```py
name = 'Zophie'
for i in name:
...     print('* * * ' + i + ' * * *')

# output
'''
* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
'''

```
