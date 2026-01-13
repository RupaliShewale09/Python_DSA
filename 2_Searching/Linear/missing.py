# Find Missing Element in 1..N (Naive)
# Example: [1,2,4,5], N=5 → Missing=3

def find_missing(arr, n):
    for num in range(1, n + 1):
        if num not in arr:
            return num
    return -1


arr = list(map(int, input("Enter array elements: ").split()))
n = int(input("Enter N: "))

print("Missing number:", find_missing(arr, n))

