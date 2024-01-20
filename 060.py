#Project Euler Problem 60
#https://projecteuler.net/problem=60

from math import isqrt
from itertools import permutations
from tqdm import tqdm

def sieve(n):
    #finds all primes under n
    bools = [True] * n
    bools[0] = False
    bools[1] = False
    for i in range(isqrt(n) + 1):
        if bools[i]:
            for j in range(i**2, n, i):
                bools[j] = False
    primes = []
    for i,val in enumerate(bools):
        if val:
            primes.append(i)
    return primes
primes = sieve(100000)

def primecheck(n):
    #checks if n is prime
    if n < 100000:
        if n in primes:
            return True
        else:
            return False
    for prime in primes:
        if n % prime == 0:
            return False
    return True


def check(a,b):
    #pairwise checks concatenations of primes
    if primecheck(int(str(primes[a]) + str(primes[b]))):
        if primecheck(int(str(primes[b]) + str(primes[a]))):
            return True
    return False

for i in range(len(primes)): # :)
    for ii in range(i): #more efficient to skip checking as soon as one permutation fails
        if check(i,ii):
            for iii in range(ii):
                if check(i,iii):
                    if check(ii,iii):
                        for iv in range(iii):
                            if check(i,iv):
                                if check(ii,iv):
                                    if check(iii,iv):
                                        for v in range(iv):
                                            if check(i,v):
                                                if check(ii,v):
                                                    if check(iii,v):
                                                        if check(iv,v):
                                                            print(sum([primes[x] for x in [i,ii,iii,iv,v]]))
                                                            exit()