# Power of a number (fast exponentiation)

"""
a^n

if n is even : a^n ==> (a^n/2)^2
if n is odd : a^n ==> (a^(n-1)/2)^2 
"""

def power(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a

        a *= a
        n //= 2
    
    return result


base = int(input("Enter base number: "))
expo = int(input("Enter exponential number: "))
print(f"{expo}th power of {base}: {power(base, expo)}")
