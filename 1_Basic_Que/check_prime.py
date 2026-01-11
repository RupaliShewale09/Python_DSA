# Check if a number is prime (optimized √N)
# O(root n)

"""
prime - divisible by only 2 factors, 1 and itself
2, 3, 5, 7, 11, 13, 17, 19

loop 2  to  sq. root of num  + 1 
--  if the no. is not prime it must have at least one factor which is < root of num
"""


def is_prime(num):
    if num <= 1:
        return False
    
    end = int(num ** 0.5)

    for i in range(2, end + 1):
        if num % i == 0:
            return False
        
    return True


num = int(input("Enter number: "))
if is_prime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is not prime")
