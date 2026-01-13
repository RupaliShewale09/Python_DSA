def substring_search(s, key):
    n, m = len(s), len(key)

    for i in range(n - m + 1):
        if s[i:i+m] == key:
            return i
    return -1


s = input("Enter string: ")
key = input("Enter substring: ")

idx = substring_search(s, key)
print("Found at index:", idx)
