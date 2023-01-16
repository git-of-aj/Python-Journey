'''
link : `https://www.hackerrank.com/challenges/py-hello-world/problem?isFullScreen=true`
'''
 print "Hello, World!"

 # LEVEL 2
 
 # Python evaluates from left to right
 # TAke input --> remove whitespaces from left --> Captilize first letter (title) -> seperate them using white space
 name1,name2 = input('Please enter your name: ').lstrip().title().split(' ')
 
 # print f with format
print(f"Nice to meet you {name1} with surname {name2}")
