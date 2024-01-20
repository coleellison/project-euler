#Project Euler Problem 84
#https://projecteuler.net/problem=84

n = 28433
for i in range(7830457):
    n *= 2
    n = n % (10 ** 10) #only store the last 10 digits

n += 1 #add one to get to the mersenne prime

print(n)