# Count digits in a number
# O(d)  d is digits

"""
num = 1234
count = 0
num = 1234 // 10 = 123   count = 1
num = 123 // 10 = 12     count = 2
num = 12 // 10 = 1       count = 3
num = 1 // 10 = 0        count = 4
"""

def count_digits(num):
    num = abs(num)
    count = 0

    while num > 0:
        num //= 10
        count += 1
    
    return count

num = int(input("Enter number:"))
print(f"There are {count_digits(num)} digits in {num}")
