#Project Euler Problem 76
#https://projecteuler.net/problem=76

pent = lambda n: (n * (3 * n - 1) // 2)
pents = []
for i in range(1,9): #pent(-8) == 100
    pents.append(pent(i))
    pents.append(pent(-1 * i))

partitions = [0 for i in range(100)] #provide some breathing room to avoid index errors
partitions.append(1)
for i in range(101, 201):
    currterm = 0
    for j,val in enumerate(pents): #recursive partition formula using pentagonal numbers
        if j % 4 > 1:
            currterm -= partitions[i - val]
        else:
            currterm += partitions[i - val]
    partitions.append(currterm)
print(partitions[-1] - 1) #exclude monomial partitions (i.e. n is a partition of n but invalid in this problem)