# Print all factors of a number
# O(root n)

"""
12 => 1, 2, 3, 4, 6, 12
20 => 1, 2, 4, 5, 10, 20

36 => 1,  36
      2,  18
      3,  12
      4,  9
      6               -- perfect sq.
"""

def factors(num):
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if i * i == num:       # for perfect square
                print(i)
            else:   
                print(i, num // i)


n = int(input("Enter number: "))
print(f"Factors of {n} :")
factors(n)