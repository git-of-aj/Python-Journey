# Problem - https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stamp = set()
for i in range(n):
    stamp.add(input())
    
print(len(stamp))
    
