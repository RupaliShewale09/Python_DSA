"""
[1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
 0  1  2  3  4  5  6  7   8   9

 x = 3                      low = 0  high = 9
 0 < 9   mid = 4  ans = 4    0           3
 0 < 3      1       4        2           3
 2 < 3      2       2        2           2
 2 <= 2     


 x = 9                        0         9
 0 < 9     4        0         5         9
 5 < 9     7        7         5         6
 5 < 6     5        7         6         6
 6 = 6     6                  7         6
"""

# Search insert position - arr[i] ≥ target
# index where the target should be inserted so that the array remains sorted.

# CEIL : Smallest no. in array >= x

def lower_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = 0

    if x > arr[high]:
        return len(arr)
    
    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))

print(f"Lower Bound : {lower_bound(arr, key)}")

