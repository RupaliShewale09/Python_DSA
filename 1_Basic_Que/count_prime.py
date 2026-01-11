# Count primes ≤ N (Sieve concept)
# O(n. log(log(n)))

"""
Sieve concept -- efficient method to find all prime num upto n

1. assume all numbers are prime  
2. start from 2, mark all multiples of prime as not prime
3. 2 prime -- mark 4, 6, 8 as non-prime
   3 prime -- mark 6, 9 as non prime
4. all left are prime
"""

def count_prime(num):
    prime = [True] * (num + 1)          # O(n)
    prime[0] = prime[1] = False

    p = 2
    while p <= int(num ** 0.5):          # O(root n)
        if prime[p]:
            for multi in range(p * p, num + 1, p):     # multiples of p (2, 11, 2)
                prime[multi] = False
            
        p += 1

    return sum(prime)

N = int(input("Enter N: "))
print(f"Count of primes <= {N} : {count_prime(N)}")