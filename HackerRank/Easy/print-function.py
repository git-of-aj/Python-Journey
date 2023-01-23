# for starts with 0 and ends with n-1 
def factorial(n):
    for num in range(n):
        print(num+1,end="")
# add +1 above to override default behaviour of for function
# the variable num takes values {0} +1 then {1} +1 ...

if __name__ == '__main__':
    n = int(input())
    factorial(n)
