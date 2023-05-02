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

# number for set
'''doctest
No.: 2
space seperated: 2 3 4 5
{2, 3, 4, 5} => set creaed
'''
#print(a)

# KNOWN ISSUES:
# - if you give spaces at end no issues
# - if you give space with map function, raises erorr that map can't int a space
# this araise valueErorr
try:
    def set_creator():
        n1 = int(input("No for set creation: "))
        myset = set()
        for _ in range(n1):
            num = input("Enter a number: ")
            try:
                myset.add(int(num))
            except ValueError:
                print(f"Error: Please enter {n1} integer.")
                #return set_creator()
        return myset

    a = set_creator()
    b = set_creator()

    union = a.union(b)
    intersection = a.intersection(b)

    for num in sorted(union.difference(intersection)):
        print(num)


except ValueError:
    print("Error: please ensure no spaces at the end")
    raise SystemExit

finally:
    print("Thanks !!")




# SystemExit asks the terminal to exit program
# finally block always run ==> for sucess and failures
# means if try block runs + except block ==> finally always run


# print("set a: ",a,"set-b: ", b) 

# symmetric difference means = union - intersection

# print(sorted(union.difference(intersection)))






