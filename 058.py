#Project Euler Problem 58
#https://projecteuler.net/problem=58

#sieve of eratosthenes
bools = [True] * 1000000
bools[0] = False
bools[1] = False
for i in range(1001):
    if bools[i]:
        for j in range(i ** 2, 1000000, i):
            bools[j] = False
primes = []
for i,val in enumerate(bools):
    if val:
        primes.append(i)

def primecheck(n):
    #check if a number is prime
    for prime in primes:
        if prime >= n: #just compare it against prime list if within range
            return 1
        if n % prime == 0: #otherwise we'll check divisibility
            return 0
    return 1

size = 3
primecount = 3
while primecount * 10 > (size * 2 - 1): #10% are primes
    size += 2 #next ring of numbers
    leg = size - 1 #distance from corner to corner
    primecount += primecheck(size ** 2 - leg)
    primecount += primecheck(size ** 2 - 2 * leg)
    primecount += primecheck(size ** 2 - 3 * leg)
    #we don't need to check the fourth corner. it's always a perfect square

print(size)