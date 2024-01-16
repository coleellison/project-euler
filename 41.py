#Project Euler Problem 41
#https://projecteuler.net/problem=41

from itertools import permutations
from math import isqrt

"""
We know that no pandigital primes of length 8 or 9 exist because they will be divisible by 3
Thus, we only need to check for factors under the square root of the maximum value
"""
largest_factor = int(7654321 ** .5)

prime_list = []

def sieve(n): #sieve of eratosthenes
    """
    Parameters
    ----------
    n : int
        upper limit

    Returns
    -------
    list
        all primes below n
    """
    bools = [True for i in range(n)]
    bools[0] = False
    bools[1] = False
    for i in range(isqrt(n) + 1):
        if bools[i]:
            for j in range(i ** 2, n, i):
                bools[j] = False
    primes = []
    for i, val in enumerate(bools):
        if val:
            primes.append(i)
    return primes

def prime_check(n):
    """
    Parameters
    ----------
    n : int
        input number

    Returns
    -------
    bool
        True if the number is prime, False if not
    """
    for factor in prime_list:
        if n % factor == 0:
            return False
    return True

prime_list = sieve(isqrt(7654321)) #we only need to check for factors up to the square root of the largest number

perm_tuples = (i for i in permutations("1234567", 7)) #itertools.permutations outputs as tuple
perms = [int("".join(perm)) for perm in perm_tuples] #convert to strings
perms.sort(reverse = True) #descending order

for num in perms:
    if prime_check(num):
        print(num)
        break #only print the first prime

