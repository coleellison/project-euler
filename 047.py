#Project Euler Problem 47
#https://projecteuler.net/problem=47

bools = [True for i in range(1000000)] #sieve of eratosthenes
bools[0] = False
bools[1] = False
for i in range(1001):
    if bools[i]:
        for j in range(i ** 2, 1000000, i):
            bools[j] = False
primes = []
for i, val in enumerate(bools):
    if val:
        primes.append(i)

factor_counts = [0 for i in range(1000000)] #pseudo-sieve for calculating factor counts
for prime in primes:
    for i in range(prime, 1000000, prime):
        factor_counts[i] += 1

for i in range(999996):
    if factor_counts[i:i+4] == [4,4,4,4]: #checks that the four consecutive values are all four
        print(i)
        break
