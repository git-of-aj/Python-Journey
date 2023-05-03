# Prob: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

# solution:
 
def average(array):
    # your code goes here
   distinct_num = set(array)
   average_of_set = sum(distinct_num) / len(distinct_num)
   return average_of_set


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
    
# logic :

n = int(input("Enter a positive number: "))
distinct_numbers = set(map(int, input("Enter space-separated integers: ").split()))

average = sum(distinct_numbers) / len(distinct_numbers)
print("set value is ", distinct_numbers,"The average of distinct numbers is:", average)


# extra :

# ask for input 
total_num = int(input("Numbre; "))


# accept only those number of input
'''
num_list = []
for i in range(total_num):
    num_list.append(int(input("Value: ")))
    '''
    
print(num_list)
# average = sum of distinct hright / total number of distinct 

user_value = map(int,input("Value Pls: ").split(" "))
print(set(user_value))
  
a = {1,2,3,4,5}
for n in a:
    # match = int(input("match: "))
    if n == int(input("match: ")):
        print("gotcha")
    else:
        break
