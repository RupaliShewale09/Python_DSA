# Count  Number of Occurrences and find them

def count(arr, key):
    c = 0
    idx = []
    for i in range(len(arr)):
        if arr[i] == key:
            idx.append(i)
            c += 1
        
    return c, idx


arr = list(map(int, input("Enter array elememts: ").split()))
key = int(input("Enter key: "))
c, idx = count(arr, key)
print(f"{key} appears in array {c} times at {idx}")