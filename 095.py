#Project Euler Problem 95
#https://projecteuler.net/problem=95

from math import sqrt,isqrt

def divsum(n):
    #sum of the divisors of n
    total = 1
    for i in range(2,isqrt(n)):
        if not n % i:
            total += i
            total += n // i
    if sqrt(n) == isqrt(n):
        total += isqrt(n) #avoid double counting perfect squares
    return total
divlist = []

for i in range(1,1000000):
    curr = divsum(i)
    count = 1
    while curr != i:
        if curr > 1000000:
            count = 100 #avoid iterating forever on convergent divisor sums
            break
        curr = divsum(curr)
        count += 1
        if count == 100:
            break
    if count == 100:
        divlist.append((0, i)) #avoid considering sequences that don't repeat
    else:
        divlist.append((count,i)) #tuple of frequency and value
divlist = sorted(divlist, reverse = True)
best = divlist[0][0] #the longest chain length
chain = []
for term in divlist:
    if term[0] == best: #find the minimum value of the longest chain
        chain.append(term[1])
chain.sort()

print(chain[0])