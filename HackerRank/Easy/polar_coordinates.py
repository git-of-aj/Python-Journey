# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
if user_input[1] == 'j':
    real = user_input[0]
    img = user_input[2]
else:
    print("Invalid")
'''
import cmath
z = complex(input())
# Use complex() to convert input to a complex number

# Check if z.real + z.imag*1j is equal to the input complex number
if z == complex(z.real, z.imag):
    print(abs(z))
    # without importing cmath raises nameerror phase not found
    print(cmath.phase(z))
else:
    print("Invalid input")
