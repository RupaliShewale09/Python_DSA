## Find last occurence of the key

def last_occurrence(arr, key):
    idx = -1
    for i in range(len(arr)):
        if arr[i] == key:
            idx = i

    return idx

arr = list(map(int, input("Enter array elememts: ").split()))
key = int(input("Enter key: "))
a = last_occurrence(arr, key)

if a != -1:
    print(f"Last occurrence of {key} in array at idx {a}")
else:
    print("Key not found")

