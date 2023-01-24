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
