#Project Euler Problem 78
#https://projecteuler.net/problem=78

pent = lambda n: (n * (3 * n - 1) // 2)
pents = []
for i in range(1,1000): #generate plenty enough pentagonal numbers
    pents.append(pent(i))
    pents.append(pent(i * -1))

partitions = [1]
while partitions[-1] % 1000000 != 0: #iterate over partitions until condition met
    currterm = 0
    for j,val in enumerate(pents):
        if val > len(partitions): #avoid indexerrors
            break
        if j % 4 > 1:
            currterm -= partitions[len(partitions) - val]
        else:
            currterm += partitions[len(partitions) - val]
    partitions.append(currterm % 1000000) #we only care about the last 6 digits
print(len(partitions) - 1) #exclude 0