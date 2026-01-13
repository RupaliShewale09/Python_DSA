"""
bitwise even odd: 
n = 13 => 1101     -- 
1101 & 0001 => 0001

n = 12 => 1100
1100 & 0001 => 0000
"""

def is_even(n):
    if n & 1:
        return "ODD"
    else:
        return "EVEN"
    
n = int(input("Enter a number: "))
print(f"Number is {is_even(n)}")