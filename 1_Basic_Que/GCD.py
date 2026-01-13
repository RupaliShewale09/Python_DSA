# using loop, O(min(a, b))
def gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    return gcd


# without % : O(max(a, b))
def gcd_sub(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"GCD of 2 numbers: {gcd(a,b)}")