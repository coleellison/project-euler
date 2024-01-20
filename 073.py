#Project Euler Problem 73
#https://projecteuler.net/problem=73

from math import gcd

total = 0
for i in range(12001):
    lower = i // 3 + 1 # numerator for 1/3 approximation
    upper = i // 2 + 1 # numerator for 1/2 approximation
    num = [j for j in range(lower, upper)] #all numerators within the bounds
    for k in num:
        if gcd(k, i) == 1: #ensure we have reduced proper fractions
            total += 1

print(total - 1) #avoid counting 1/2 itself