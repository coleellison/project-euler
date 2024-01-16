#Project Euler Problem 45
#https://projecteuler.net/problem=45
from time import time
#we can ignore triangular numbers - every hexagonal number is also triangular

pent = 40755
hex = 40755
p = 165
h = 143

"""
pent(n+1) - pent(n) = ((3n^2 + 6n + 3 - n - 1) - (3n^2  - n)) / 2 = 3n + 1
hex(n+1) - hex(n) = (2n^2 + 4n + 2 - n - 1) - (2n^2 - n) = 4n + 1
"""

nextpent = lambda curr: curr + 3 * p + 1
nexthex = lambda curr: curr + 4 * h + 1

pent = nextpent(pent)
hex = nexthex(hex)
p += 1
h += 1

while pent != hex:
    if pent > hex:
        hex = nexthex(hex)
        h += 1
    else:
        pent = nextpent(pent)
        p += 1
print(pent)