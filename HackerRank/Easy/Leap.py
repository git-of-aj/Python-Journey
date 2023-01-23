# ------------------------------------------------------------------------------------
# any year divisible by 400 and 4 is a leap year
# -----------------------------------------------------------------------------------


# HACKER RANK SAYS THE YEAR DIVIDED BY 4 IS LEAP AS LONG AS IT IS NOT CLEARLY DIVISIBLE BY 100
# AND A YEAR DIVISIBLE BY 400 IS SURELY LEAP

#-----------------------------------------------------------------------------
# THIS WORKS

def is_leap(year):
    leap = False
    # Write your logic here
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 400 == 0):
        return True
    else:
        return False 
    
    return leap

year = int(input()).strip()



#--------------------------------------------------------------------
year = int(input())
#return year

# creating a function is_leap to identify leap year from given input

def is_leap() :
    if year%4 == 0 :
        if year%400 == 0 :
            print(f'{year} is a leap year')
    else :
    print(f'{year} is not a leap year')

# --------------

# 2 method

year = int(input())
return year

def is_leap(year) :
    if (year%4 == 0) or (year%400 == 0) :
        print('year is a leap year')
    else :
        print('Not a leap year')
