#Project Euler Problem 25
#https://projecteuler.net/problem=25

fiblist = [1, 1] #base case

while len(str(fiblist[-1])) < 1000: #while the number is less than 1000 digits
    fiblist.append(fiblist[-1] + fiblist[-2]) #generate a new fibonacci number
print(len(fiblist)) #count how many iterations it took