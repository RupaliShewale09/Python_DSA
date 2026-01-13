# Check if Array is Sorted

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return 0
        
    return 1

arr = list(map(int, input("Enter array elements:").split()))
if is_sorted(arr):
    print("Array is sorted")
else:
    print("Array is not sorted")


    
