# GCD of two numbers (Euclidean Algorithm) 
# O(log(min(a,b)))

"""
GCD of 2 numbers is the largest number that divides both numbers exactly

Euclidean Algo: GCD(a, b) = GCD(b, a % b)
- Replace the bigger number with the remainder until the remainder becomes 0.

GCD(48, 18)

Divide 48 by 18
48 % 18 = 12
→ GCD(48, 18) = GCD(18, 12)

Divide 18 by 12
18 % 12 = 6
→ GCD(18, 12) = GCD(12, 6)

Divide 12 by 6
12 % 6 = 0

GCD = 6
"""

def gcd_euclidean(a, b):
    while b != 0:
        r = a % b
        a, b = b , r
    
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"GCD of 2 numbers: {gcd_euclidean(a,b)}")

