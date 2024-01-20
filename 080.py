#Project Euler Problem 80
#https://projecteuler.net/problem=80

from math import isqrt
sigfig = 100
total = 0
for num in range(1,101):
    if int(num ** .5) ** 2 != num: #check for perfect square
        total += sum(int(i) for i in str(isqrt(num * 10 ** (2 * (sigfig - 1))))) #multiplies by 10 ** 2(sigfig) - 1 to ensure enough significant figures for square root
print(total)

