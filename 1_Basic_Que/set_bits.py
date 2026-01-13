# count set bits in a number

"""
set bits = 1
n = 13 → 1101 → 3 set bits

n & (n - 1) removes the rightmost set bit.

1101 & 1100  --> 1100  
1100 & 1010  --> 1000
1000 & 0111  --> 0000 
"""

def count_set_bits(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

print(count_set_bits(13))
