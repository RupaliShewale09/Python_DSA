# O(n . root n)

def is_prime(num):
    if num <= 1:
        return False
    
    end = int(num ** 0.5)

    for i in range(2, end + 1):
        if num % i == 0:
            return False
        
    return True


def range_prime(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)
        
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(f"\nPrime numbers between {start} and {end} : ")
range_prime(start, end)