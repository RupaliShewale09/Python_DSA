# Find Duplicate Using Linear Search
# Example: [1, 2, 3, 2, 4] → 2

def duplicate(arr):
    dup = []
    for char in arr:
        if char in dup:
            return char
        else:
            dup.append(char)
    
    return None

arr = list(map(int, input("Enter array elememts: ").split()))
a = duplicate(arr)
if a:
    print(f"{a} is duplicate")
else:
    print("No element is duplicate")
