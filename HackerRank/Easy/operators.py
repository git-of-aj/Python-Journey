'''
problem link: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
'''
# take multiple inputs ; split them by whitespaces ; int can map only one input at a time so use map for multiple inputs

# version2 
x,y=map(int,input("Please enter 2 numbers, seperated with comma(,): ").split(','))
print(f'{x+y} \n{x*y} \n{x-y}')

# version1 
x,y=map(int,input().split())
print(f'{x+y} \n{x*y} \n{x-y}')

# print without specifying variables 
#print(f'{x+y},{x*y},{x-y}')


# NORMAL PEOPLE (HACKERRANK ANSWER)
# take input 
a = int(input())
b = int(input())

# add 
print(a+b)
# subtarct
print(a-b)
# multiply
print(a*b)
