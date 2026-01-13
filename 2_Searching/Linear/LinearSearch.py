## Linear Search

def linear(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    
    return -1

arr = list(map(int, input("Enter array elememts: ").split()))
key = int(input("Enter key: "))

a =  linear(arr, key)
if a != -1:
    print(f"Key found at index {a}")
else:
    print("Key Not found")