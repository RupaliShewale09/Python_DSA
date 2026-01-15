def binary_search(arr, low, high, key):
    if low > high:
        return -1

    # mid = (low + high) // 2          -- can cause overflow
    mid = low + (high - low) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, mid + 1, high, key)
    else:
        return binary_search(arr, low, mid - 1, key)
    

arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))

idx = binary_search(arr, 0, len(arr) -1, key)

if idx != -1:
    print(f"Key found at index {idx}")
else:
    print("Key not found")
