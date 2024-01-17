#Project Euler Problem 7
#https://projecteuler.net/problem=7

primelist = [2]
n = 2
while len(primelist) < 10001: #loops until we have found the 10001st prime
    prime = True #flag to keep track of if a factor is found.
    for x in primelist:
        if n % x == 0:
            prime = False #factor has been found
            break
    if prime == True: #evaluates to true if a factor has not been found
        primelist.append(n)
    n += 1
print(primelist[-1]) #the last term will be the 10001st term.
