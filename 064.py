#Project Euler Problem 64
#https://projecteuler.net/problem=64

from decimal import *

getcontext().prec = 1000 #ensure sqrt() is sufficiently accurate


total = 0
for x in range(1,10001):
    if int(x ** .5) ** 2 == x: #ignore perfect squares
        continue
    n = Decimal(x).sqrt()
    l = []
    for i in range(1000): #ensure enough sigfigs
        l.append(int(n))
        n -= int(n)
        n = 1/n
    l.pop(0)
    dist = 1

    dists = []
    while dist < len(l) // 2:
        if l[:dist] == l[dist:2*dist]: #the first n digits match the next n digits
            dists.append(dist) #correct pattern
        dist += 1
    dist = dists[-1] - dists[-2]
    if dist % 2 == 1: #odd period
        total += 1
print(total)