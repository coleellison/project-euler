#Project Euler Problem 2
#https://projecteuler.net/problem=2

limit = 4000000 #ensures numbers do not exceed 4 million
fibonacci = [1,1] #base case

while fibonacci[-1] <= limit:
    fibonacci.append(fibonacci[-1] + fibonacci[-2]) #generate new term
fibonacci.remove(fibonacci[-1]) #removes the final term which exceeds the limit

total = 0
for x in fibonacci:
    if x % 2 == 0 : #if even
        total += x

print(total)