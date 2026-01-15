"""
[2, 4, 6, 8, 8, 8, 11, 13]
 0  1  2  3  4  5   6   7

x = 8 {3, 5}
x = 10 {-1, -1}
x = 11 {6, 6}

## METHOD 1 : using LB and UB

lower bound => arr[i] >= key    for x = 8 i.e 3
So first occurrence same
but for x = 10    LB = 6    it is not present so first occ = -1

upper bound => arr[i] > key    i.e 6
So last occurence = upper bound - 1 = 5
"""


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

def upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = 0

    if x >= arr[high]:
        return len(arr)
    
    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def First_last(arr, x):
    UB = upper_bound(arr, x) - 1
    LB = lower_bound(arr, x)

    if LB == len(arr) or arr[LB] != x or UB == len(arr) or arr[UB] != x:
        return -1, -1
    
    return LB, UB



arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))
first, last = First_last(arr, key)
print(f"First occurence of {key} : {first}")
print(f"Last occurence of {key} : {last}")