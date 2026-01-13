# Find Minimum & Maximum in Array

def min_max(arr):
    min_val = float('inf')
    max_val = float('-inf')

    for char in arr:
        if char > max_val :
            max_val = char
        if char < min_val :
            min_val = char
    
    return min_val, max_val

arr = list(map(int, input("Enter array elememts: ").split()))
min_val, max_val = min_max(arr)
print(f"Min : {min_val}\nMax : {max_val}")

