# Check if a number is palindrome
# O(d)

"""
Working:  12321 => palindrome    123 => not
1. reverse
2. if reverse == num then palindrome
"""

def revnum(num):
    rev = 0
    while num > 0:
        d = num % 10
        rev = (rev * 10) + d
        num //= 10

    return rev

def palin_num(num):
    rev = revnum(num)

    if num == rev:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

num = int(input("Enter number: "))
palin_num(num)