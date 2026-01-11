# Check Armstrong number
# O(d)  d = digits
# O(log10(n))

"""
153 => 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153    yes
9474 => 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474   yes
123 => 1^3 + 2^3 + 3^3 = 36   no

arm_num = 0
num = temp = 153  length = 3
digit = 153 % 10 = 3       arm_num = 0 + digit ** length = 3 ** 3 = 27
temp = 153 // 10 = 15  

digit = 15 % 10 = 5       arm_num = 27 + 5 ** 3 = 152
temp = 15 // 10 = 1 

digit = 1 % 10 = 1       arm_num = 152 + 1 ** 3 = 153
temp = 1 // 10 = 0
"""

def check_arm(num):
    temp = num
    length = len(str(num))
    arm_num = 0

    while temp > 0:        # runs once per digit
        digit = temp % 10
        arm_num += digit ** length
        temp //= 10

    if num == arm_num:
        return 'Armstrong'
    
    return 'Not Armstrong'
    
num = int(input("Enter a number: "))
print(f"{num} is {check_arm(num)}")