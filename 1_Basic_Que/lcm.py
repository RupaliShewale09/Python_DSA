# LCM of two numbers

"""
LCM : smallest number that is exactly divisible by both numbers

multipliers of 4 --> 4, 8, 12, 16
multipliers of 6 --> 6, 12, 18

formula : (a * b)//gcd(a,b)
"""

def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b , r
    
    return a

def lcm(a, b):
    return (a * b)//gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("LCM of 2 numbers: ", lcm(a, b))