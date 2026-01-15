
def first_occ(arr, x):
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return first



def last_occ(arr, x):
    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] == x :
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return last

def pair(arr, x):
    first = first_occ(arr, x)
    if first == -1:
        return -1, -1
    
    last = last_occ(arr,x)
    return first, last


arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))
first, last = pair(arr, key)
print(f"First occurence of {key} : {first}")
print(f"Last occurence of {key} : {last}")