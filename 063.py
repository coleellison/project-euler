#Project Euler Problem 63
#https://projecteuler.net/problem=63

def nthpowers(N):
    #how many n-digit numbers can be written as powers of n
    exp = (N - 1)/N
    numpowers = int(10 - 10 ** exp)
    return numpowers

total = 0
n = 1
while nthpowers(n) != 0: #will converge to 0 as n grows
    total += nthpowers(n)
    n += 1

print(total)