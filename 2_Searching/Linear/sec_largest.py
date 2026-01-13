# Find Second Largest 

def sec_largest(arr):
    if len(arr) < 2:
        return None
    
    first = float("-inf")
    second = float("-inf")

    for char in arr:
        if char > first:
            second = first
            first = char
        elif char > second and char != first:
            second = char
    
    if second == float('-inf'):
        return None
    
    return second

def sec_smallest(arr):
    if len(arr) < 2:
        return None
    
    first = float("inf")
    second = float("inf")

    for char in arr:
        if char < first:
            second = first
            first = char
        elif char < second and char != first:
            second = char
        
    if second == float("inf"):
        return None
    
    return second
    
arr = list(map(int, input("Enter array elememts: ").split()))
print(f"Second largest element in array: {sec_largest(arr)}")
print(f"Second smallest element in array: {sec_smallest(arr)}")