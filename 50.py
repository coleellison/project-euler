#Project Euler Problem 50
#https://projecteuler.net/problem=50

bools = [True] * 1000000 #sieve of eratosthenes
bools[0] = False
bools[1] = False
for i in range(1001):
    if bools[i]:
        for j in range(i**2, 1000000, i):
            bools[j] = False
primes = []
for i,val in enumerate(bools):
    if val:
        primes.append(i)

longest = 0 #find the longest sequence of primes that can sum under 1000000
total = 0
for prime in primes:
    if total + prime < 1000000:
        total += prime
        longest += 1
    else:
        break

finished = False
for length in range(longest, -1, -1): #check every iteration of sums that amount to under 1000000, ordered from longest to shortest
    i = 0
    if finished:
        break
    while sum(primes[i:i + length]) < 1000000: #decrements length once all sums under 1000000 are exhausted
        if sum(primes[i:i + length]) in primes:
            print(sum(primes[i:i + length]))
            finished = True
            break
        i += 1