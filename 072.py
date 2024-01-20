# Project Euler Problem 72
# https://projecteuler.net/problem=72

from math import ceil
from tqdm import tqdm

def sieve(n):
    #finds all primes under n
    bools = [True for i in range(n)]
    bools[0] = False
    bools[1] = False
    for i in range(ceil(n ** .5)):
        if bools[i]:
            for j in range(i ** 2, n, i):
                bools[j] = False
    return [i for i,val in enumerate(bools) if val]

primes = sieve(1000000)

def phi(n):
    #euler's totient function
    totient = n
    for prime in primes:
        if prime > n:
            return int(totient)
        elif n % prime == 0:
            totient *= (prime - 1) / prime

upperlimit = 1000000
total = 0
for i in range(2,upperlimit + 1): #slow runtime :(
    total += phi(i)
print(total)