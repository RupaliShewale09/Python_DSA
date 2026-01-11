# Reverse a number
# O(d)

"""
Working:  123 ==> 321
num = 123
d = 123 % 10 => 3       rev = 0*10 + 3 => 3
num = 123 // 10 => 12
d = 12 % 10 => 2       rev = 3*10 + 2 => 32
num = 12 //10 => 1
d = 1 % 10 => 1        rev = 32*10 + 1 => 321
num = 1 // 10 => 0 
"""

## butt 100 should be 001 but it will 1
# if we wantt 00 we can check len -- 
# if len of reverse is less then zfill-- but will string

def revnum(num):
    sign = -1 if num < 0 else 1
    num = abs(num)

    rev = 0
    while num > 0:
        d = num % 10
        rev = (rev * 10) + d
        num //= 10

    return sign * rev

num = int(input("Enter a number: "))
print(f"Reverse of {num}: {revnum(num)}")