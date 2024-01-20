#Project Euler Problem 94
#https://projecteuler.net/problem=94

from math import gcd

def euclid(m,n):
    #generates right triangle using Euclid's method
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return (a,b,c)

total = 0
for a in range(2,20000):
    for b in range(1,a):
        if (a + b) % 2 == 1: #one even, one odd
            if gcd(a,b) == 1: #relatively prime
                legs = sorted(euclid(a,b))
                if (legs[2] + legs[0]) * 2 > 10 ** 9: #perimeter too large
                    break
                if abs(legs[0] * 2 - legs[2]) == 1: #"almost equilateral" condition
                    total += (legs[2] + legs[0]) * 2
print(total)