#Project Euler Problem 40
#https://projecteuler.net/problem=40

#Brute force approach is very fast
bigstring = ""
i = 1
while len(bigstring) < 1000000: #ensures we do not create a string longer than needed
    bigstring += str(i)
    i += 1

digits = [bigstring[0], bigstring[9], bigstring[99], bigstring[999], bigstring[9999], bigstring[99999], bigstring[999999]] #desired indices

product = 1
for digit in digits:
    product *= int(digit) #multiply them

print(product)
