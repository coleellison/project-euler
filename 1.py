#Project Euler Problem 1
#https://projecteuler.net/problem=1

total = 0

for i in range(1000): #first thousand non-negative integers
    if (i % 3 == 0 or i % 5 == 0): #divisible by 3 or 5
        total += i #add the the sum

print(total)