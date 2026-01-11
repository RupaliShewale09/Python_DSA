# count all factors of a number
# O(root n)

"""
25 => 1, 5, 25 => 3   
"""

def count_factors(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if i * i == num:       # for perfect square
                count += 1
            else: 
                count += 2

    return count    


n = int(input("Enter number: "))
print(f"Number of factors of {n} : {count_factors(n)}")  