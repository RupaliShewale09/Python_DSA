"""
arr = 10 20 30 40 50 60 70    key 50

low = 0    high = 6      
0 < 6      mid = 3    arr[3] = 40 < 50    low = 3+1 = 4
4 < 6      mid = 5    arr[5] = 60 > 50    high = 5-1 = 4
4 = 4      mid = 4    arr[4] = 50 = 50 

"""

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # mid = (low + high) // 2          -- can cause overflow
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))

idx = binary_search(arr, key)

if idx != -1:
    print(f"Key found at index {idx}")
else:
    print("Key not found")