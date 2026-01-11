# Sum of digits of a number
# O(d)

"""
num = 123  sum => 6

sum = 0
sum = (123 % 10) + 0 => 3     
num = 123 // 10 = 12

sum = (12 % 10) + 3 => 5
num = 12 // 10 = 1

sum = (1 % 10) + 5 => 6
num = 1 // 10 = 0
"""

def sum_digits(num):
    num = abs(num)
    sum = 0

    while num > 0:
        sum += (num % 10) 
        num //= 10
    
    return sum

num = int(input("Enter number:"))
print(f"Sum of digits : {sum_digits(num)}")


