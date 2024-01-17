#Project Euler Problem 48
#https://projecteuler.net/problem=48

print(sum((i ** i) % (10 ** 10) for i in range(1,1001)) % (10 ** 10)) #one line :)
