# Sum of Array Elements
def sum_arr(arr):
    sum = 0
    for char in arr:
        sum += char

    return sum

arr = list(map(int, input("Enter array elememts: ").split()))
print(f"Sum of array elements: {sum_arr(arr)}")