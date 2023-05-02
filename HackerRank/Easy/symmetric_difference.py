# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem

# this works:

# Enter your code here. Read input from STDIN. Print output to STDOUT
def set_creator():
    n1 = int(input(""))
    myset = set(map(int,(input("").split(" "))))
    return myset

a = set_creator()
b = set_creator()

# print("set a: ",a,"set-b: ", b) 

# symmetric difference means = union - intersection
union = a.union(b)
intersection = a.intersection(b)

# print(sorted(union.difference(intersection)))

for num in sorted(union.difference(intersection)):
    print(num)

# OPTIMISED VERSION:

