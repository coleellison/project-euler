#Project Euler Problem 23
#https://projecteuler.net/problem=23

divsum = lambda n: sum([d for d in range(1,n) if not n % d]) #outputs the proper factor sum of input n
divlist = [n for n in range(1, 21824) if divsum(n) > n] #all abundant numbers under upper bound

sums = set() #use set to avoid duplicates
for i in range(len(divlist)): #iterate over every element
    for j in range(i + 1): #iterate over every element, avoiding repeats
        total = divlist[i] + divlist[j]
        if total > 28123:
            break
        sums.add(total)
sums = tuple(sums) #convert to iterable

print(sum([n for n in range(21824) if n not in sums]))




