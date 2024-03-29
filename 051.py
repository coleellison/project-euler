#Project Euler Problem 51
#https://projecteuler.net/problem=51

from math import isqrt

def matching_digits(A, B, C):
    """checks if digits match the desired pattern between 3 numbers

    Parameters
    ----------
    A : int
        lowest prime
    B : int
        middle prime
    C : int
        prime to test if it falls under the same pattern

    Returns
    -------
    the integer pattern if C matches the pattern, False if not.
    """
    A = str(A)
    B = str(B)
    C = str(C)
    result = ""
    A_set = set()
    B_set = set()
    C_set = set()
    for i in range(len(A)):
        if A[i] == B[i] and A[i] == C[i]:
            result += "0"
        else:
            A_set.add(A[i])
            B_set.add(B[i])
            C_set.add(C[i])
            result += "1"
    if (len(A_set) > 1 or len(B_set) > 1 or len(C_set) > 1): #return False if not a valid match for the pattern
        return False
    else:
        return int(result)

n = 1000000

#sieve of eratosthenes
prime_bool = [True] * n
prime_bool[0] = False
prime_bool[1] = False

for i in range(2, isqrt(n)):
    if prime_bool[i]:
        for j in range(i ** 2, n, i):
            prime_bool[j] = False

prime_list = []
for i in range(n):
    if prime_bool[i]:
        prime_list.append(i)

#looking at 6 digit primes
i = 5
max_replacements = 0
min_range = 10 ** i
max_range = 10 ** (i + 1)

primes = []
for i in prime_list:
    if min_range < i < max_range:
        primes.append(i)

br = False

for i in range(len(primes)):
    a = primes[i]
    print(a)
    for j in range(i + 1, len(primes)): #seed the sequence with two primes
        b = primes[j]
        difference = b - a
        if set(str(difference)) != {"0","1"}: #in order to have 8 hits, we cannot increment by more than 1. (2 * 7 > 10)
            continue
        c = b + difference #new term generated by adding common difference
        total = 2
        while matching_digits(a, b, c):
            if c in primes:
                total += 1 #track how many matches
            c += matching_digits(a, b, c) #increment by the common difference
        if total > 7:
            print(a)
            exit()