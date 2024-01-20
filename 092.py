#Project Euler Problem 92
#https://projecteuler.net/problem=92

def chainbool(N):
    #returns True if the chain ends in 89, False if it ends in 1
    while N != 1 and N != 89:
        newN = 0
        for i in str(N): #sum of digits squared
            newN += int(i) ** 2
        N = newN
    if N == 89:
        return True
    else:
        return False

total = 0
for i in range(1, 10000000):
    if chainbool(i):
        total += 1

print(total)