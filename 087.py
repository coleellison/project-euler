#Project Euler Problem 87
#https://projecteuler.net/problem=87

upper = 50000000
upper2 = int(upper ** (1/2)) #maximum nth powers that fit under upper limit
upper3 = int(upper ** (1/3))
upper4 = int(upper ** (1/4))

primes2 = [2]
for i in range(3,upper2):
    prime = True
    for p in primes2:
        if i % p == 0:
            prime = False
            break
    if prime:
        primes2.append(i)

primes3 = []
primes4 = []
for i in primes2: #avoid regenerating primes
    if i < upper3:
        primes3.append(i)
    else:
        break
for i in primes3: #avoid regenerating primes
    if i < upper4:
        primes4.append(i)
    else:
        break

triples = set()
for i in primes2: #iterate over all combinations of triples
    for j in primes3:
        for k in primes4:
            val = (i ** 2 + j ** 3 + k ** 4)
            if val < upper:
                triples.add(val) #ensure we don't have any duplicates
            else:
                break

print(len(triples))
            
