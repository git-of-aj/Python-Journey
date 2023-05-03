# Problem: https://www.hackerrank.com/challenges/no-idea/problem

# USE THIS IN HACKKERRANK:


# THE BELOW IS OPTIMISED FOR YOUR OWN UNDERTSANDINH
'''
!!!!!!!! THE BELOW CODE ACCEPTS RESULTS IN DIFEERENT LINE NOT SPACE SEPERATED !!!!!!!
def set_creator(num1):
        #num1 = int(input("No for set creation: "))
        print(f"This is for {num1}")
        myset = set()
        for _ in range(num1):
            num = input("Enter a number: ")
            try:
                myset.add(int(num))
            except ValueError:
                print(f"Error: Please enter {num1} integer.")
                #return set_creator()
        return myset
'''
def set_creator(num1):
     print(f"this is for {num1}")
     myset = set()
     nums = input(f"Enter {num1} space-separated integers: ").split()

     if len(nums) != num1:
        print(f"Error: Expected {num1} integers, got {len(nums)}")
        exit()
     else:
          for i in nums:
               myset.add(i)
     return myset


def score(a,b,array):
     # check if set a elements are in the array
     happy = len(a.intersection(array))
     if happy != 0:
          good = happy
     if happy == 0:
          good = 0
     
     sad = len(b.intersection(array))
     if sad == 0:
          bad =  0
     else:
          bad = sad
     
     return (happy - sad)
          

     
     
def main():
    # input 
    n1,n2 = map(int,input("Nums for sets with space: ").split(" "))

    # second line accept n1 inputs ==> here we create array to compare
    super_set = set_creator(n1)

    # 3 line accept n2 inputs
    a = set_creator(n2)

    # fourth line accept n2 inputs
    b = set_creator(n2)

    # calculate hapiness
    print(score(a,b,super_set))

if __name__ == '__main__':
     main()
