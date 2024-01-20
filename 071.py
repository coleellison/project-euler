#Project Euler Problem 71
#https://projecteuler.net/problem=71

from math import gcd

n = 3/7
bestapprox = [0,1]
for i in range(8, 1000000):
    currentapprox = [int(i * n), i] #int(i * n) is the best numerator for a lower approximation of 3/7 with denominator i
    if gcd(currentapprox[0],currentapprox[1]) == 1: #relatively prime
        if (currentapprox[0] / currentapprox[1]) > (bestapprox[0] / bestapprox[1]): #our approximation underestimates, so we want the maximum estimate
            bestapprox = currentapprox

print(bestapprox[0]) #numerator