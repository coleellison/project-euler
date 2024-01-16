#Project Euler Problem 5
#https://projecteuler.net/problem=5

from math import lcm

n = 20 #max factor
i = 1 #minimum factor
total = 1

while i <= n:
    total = lcm(total, i) #sequentially calculate the lcm of the previous terms and the new term
    i += 1

print(total)