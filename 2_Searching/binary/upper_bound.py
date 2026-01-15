"""
ex.      0  1  2  3  4  5  6   7   8   9
arr[] = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]

x = 6                          low = 0  high = 9
0 <= 9    mid=4   8>6   ans=4     0        3
0 <= 3     1      3<6     4      2         3
2 <= 3     2      6=6     4      3         3
3 <= 3     3      7>6     3      3         2
return 3

"""


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


arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))

print(f"Upper Bound : {upper_bound(arr, key)}")