# take input 

x =  int(input())

#check non negative condition

if x > 0 :
    for i in range(x) :
        print(x^2)
else 
print('condition void')




#--------------------------------

# https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# take input 
n= int(input())
# i is a variable which takes value [0,1,...n-1]
# iterate till  i < n and sqaure 
for i in range(n):
    if i < n:
        print(i*i)
        # or print(i^2)
