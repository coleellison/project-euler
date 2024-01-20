#Project Euler Problem 100
#https://projecteuler.net/problem=100

n = 1
inc = 1
while True: #exploring for small values of n reveals the recursive generating sequence
    d = int(n * (2 ** .5))
    num = n * (n - 1)
    den = d * (d - 1)
    if num * 2 == den:
        if d > (10 ** 12):
            break
        inc = n // inc
    n += inc
print(n)