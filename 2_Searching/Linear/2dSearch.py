# Linear Search in 2D Array / Matrix

def search_2d(rows, cols, arr, key):
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == key:
                return i, j
    return -1, -1


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

key = int(input("Enter element to search: "))

r, c = search_2d(rows, cols, matrix, key)

if r != -1:
    print(f"Element found at position ({r}, {c})")
else:
    print("Element not found")
