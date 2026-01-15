"""
==> FLOOR : largest no. in array <= x
==> CEIL : Smallest no. in array >= x  (LOWER BOUND)

[10, 15, 20, 25, 30, 40]
x = 17   --> FLOOR = 15       CEIL = 20 
x = 25   --> FLOOR = 25       CEIL = 25
x = 27   --> FLOOR = 25
"""


def floor(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    
    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1

    return ans

def ceil(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    
    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))

print(f"FLOOR : {floor(arr, key)}")
print(f"CEIL : {ceil(arr, key)}")
