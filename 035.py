#Project Euler Problem 35
#https://projecteuler.net/problem=35

from math import isqrt

def sieve(n): #sieve of eratosthenes
    bools = [True for i in range(n)]
    bools[0] = False
    bools[1] = False
    for i in range(isqrt(n) + 1):
        if bools[i]:
            for j in range(i ** 2, n, i):
                bools[j] = False
    return bools

flags = ["2","4","5","6","8","0"] #these digits cannot be in a prime, because they are unacceptable ones digits of multi-digit primes.
candidates = []
for i, val in enumerate(sieve(1000000)):
    if val:
        cand = True
        for digit in str(i):
            if digit in flags: #exclude numbers with 5 or an even number in them.
                cand = False
                break
        if cand:
            candidates.append(str(i))

#2 and 5 are not digit options for multi-digit primes, but they themselves are prime.
candidates.append("2")
candidates.append("5")

circular_primes = []
for i in candidates:
    prime_count = 0
    for j in range(len(i)):
        if (i[j:] + i[:j]) in candidates: #rotate the number about index j
            prime_count += 1
    if prime_count == len(i): #if every iteration is prime
        circular_primes.append(i)

print(len(circular_primes))
