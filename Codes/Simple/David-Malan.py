# Take name
name = input("Hi 👋, What's Your name: ")
# say hello
def hello(friend):
    print("Hello,",friend,sep='')
# call that main
hello(name)

# User Flow: Name variable takes input --> Hands over that input to Friend Variable.
# if you replace hello(something-else) --> NameError coz nothing specified
