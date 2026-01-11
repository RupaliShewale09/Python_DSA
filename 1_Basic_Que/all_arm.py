# Print all Armstrong numbers in a range
# O(d * n)    d = digits

def check_arm(num):
    temp = num
    length = len(str(num))
    arm_num = 0

    while temp > 0:           # runs once per digit   O(d)
        digit = temp % 10
        arm_num += digit ** length
        temp //= 10

    return num == arm_num

def range_arm(start, end):
    for num in range(start, end+1):
        if check_arm(num):
            print(num)
        
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(f"\nArmstrong numbers between {start} and {end} : ")
range_arm(start, end)