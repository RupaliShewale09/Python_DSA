# Check if a number is perfect

"""
28  => 1, 2, 4, 7, 14 => sum 28

sum = 0         num ** 0.5 => 5
i = 1    28 % 1 == 0,     sum = 0 + 1  = 1
i = 2    28 % 2 == 0,     sum = 1 + 2 + (28//2) = 1+ 2 + 14 = 17
i = 3    28 % 3 
i = 4
i = 5 
"""

def is_perfect(num):
    sum = 0

    for i in range(1, int(num ** 0.5) + 1):
        if  num % i == 0:
            if i * i == num or i == 1:
                sum += i
            else: 
                sum += i + (num // i)
        
    return sum == num

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is perfect")
else:
    print(f"{num} is not perfect")