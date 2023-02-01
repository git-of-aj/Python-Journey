# for Hackerrank
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in
          range(z + 1) if i + j + k != n]
    print(ar)


# -------------------------------------------------------------------------------
# input
n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n3 = int(input("Enter num3: "))
not_sum = int(input("Enter sum not equal to: "))

# create poosible combinations

def combinations():
    # creates list of possiblities
    array = [[x,y,z] for x in range(n1+1) for y in range(n2+1) for z in range(n3+1) if x+y+z != not_sum]
    print(array)

# excludes the list with a+b+c == not_sum with if statement
# [x,y,z] ==> so that we can create a list to print
# not specifying any functional arguments here as n1,n2 etc are global variables so works everywher!

# return the result
combinations()
