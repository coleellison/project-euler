#Project Euler Problem 66
#https://projecteuler.net/problem=66

from math import isqrt

def solvePell(D): #source: https://rosettacode.org/wiki/Pell%27s_equation - refactored for this problem
    srD = isqrt(D) #slightly tweaked syntax to be more understandable
    a, b, r = srD, 1, srD * 2
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        a = r * b - a
        b = (D - a ** 2) // b
        r = (srD + a) // b

        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r

        x, y = f2 * srD + e2, f2
        if x ** 2 - D * y ** 2 == 1:
            return x

print(max([solvePell(i) for i in range(1,1001) if i != isqrt(i) ** 2]))