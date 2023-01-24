# Take name
name = input("Hi 👋, What's Your name: ")
# say hello
def hello(friend):
    print("Hello,",friend,sep='')
# call that main
hello(name)

# User Flow: Name variable takes input --> Hands over that input to Friend Variable.
# if you replace hello(something-else) --> NameError coz nothing specified
#-----------------------------------------------------------------------------------------------------------

# say hello
def hello(friend):
    friend = input("Hi 👋, What's Your name: ")
    print("Hello,",friend,sep='')
# call that main
hello(friend = "World") # specifying argument here.... instead of inside function
# if you delete input .. Prints Hello World
# more: https://www.freecodecamp.org/news/python-function-examples-how-to-declare-and-invoke-with-parameters-2/


#---------------------------
'''
# Joining with empty separator
list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))
# the above prints geeks

'''
# Joining with string
list1 = " geeks "
print("$".join(list1))
# the above prints = $g$e$e$k$s$ ==> $ in begin & end = space

#--------------------------------------------------------------------

string = "abracadabra"
l = list(string)
# replace a with k
l[5] = 'k'

string = ''.join(l)
# '' => means add no space nothing b/w every item of variable l
# join function joins elements of a sequence and makes it a string.
# if the iterable contains any non-string values, it raises a TypeError exception.  
print(string)
