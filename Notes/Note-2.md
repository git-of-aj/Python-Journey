> Lists and tuples can contain multiple values, which makes writing programs that handle large amounts of data easier.

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
