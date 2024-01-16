#Project Euler Problem 37
#https://projecteuler.net/problem=37

from math import isqrt

def sieve(n): #sieve of eratosthenes
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

def left_trunc(num):
    """
    Parameters
    ----------
    num : int
        the inputted prime

    Returns
    -------
    bool
        returns True if every left truncation is prime, else False
    """
    while num > 10: #avoid indexing errors
        if num in prime_list:
            num = int(str(num)[1:])
        else:
            return False
    if num in prime_list:
        return True
    
def right_trunc(num):
    """
    Parameters
    ----------
    num : int
        the inputted prime

    Returns
    -------
    bool
        returns True if every right truncation is prime, else False
    """
    while num > 10: #avoid indexing errors
        if num in prime_list:
            num = int(str(num)[:-1])
        else:
            return False
    if num in prime_list:
        return True

trunc_primes = []
#Significantly large primes are increasingly less likely to meet the desired conditions.
prime_list = sieve(1000000)
for i in prime_list: #check all primes
    if left_trunc(i) and right_trunc(i): #Both left and right truncations must be met
        if i > 10:
            trunc_primes.append(i) #one digit primes are not eligible

#print(len(trunc_primes)) #ensure we found all 11
print(sum(trunc_primes)) #result
