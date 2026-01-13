# find trailing zeros in factorial

"""
10! = 3628800 → 2 trailing zeros
trailing zeros appear when multiplied by 10 - (2*5)
2 are plenty but 5 are rare so 
Number of trailing zeros = number of times 5 appears
c = 0  

"""

def trailing_zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

n = int(input("Enter a number:"))
print(f"There are {trailing_zeros(n)} trailing zeros in {n}!")
