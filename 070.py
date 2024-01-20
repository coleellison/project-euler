#Project Euler Problem 70
#https://projecteuler.net/problem=70

from math import ceil

def sieve(n):
    #all primes under n
    bools = [True for i in range(n)]
    bools[0] = False
    bools[1] = False
    for i in range(ceil(n ** .5)):
        if bools[i]:
            for j in range(i ** 2, n, i):
                bools[j] = False
    primes = [i for i,val in enumerate(bools) if val]
    return primes

best = (2,0) #keep track of the best ratio and its corresponding n
primes = sieve(1000000)
for i in range(len(primes)): #find pairs of primes
    for j in range(i):
        product = primes[i] * primes[j]
        if product > 10 ** 7: #out of range, try new i
            break
        phi = (primes[i] - 1) * (primes[j] - 1)
        if sorted(str(product)) == sorted(str(phi)):
            best = min(best, (product / phi, product))

print(best[1])
