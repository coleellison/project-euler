#Project Euler Problem 28
#https://projecteuler.net/problem=28

size = 1 #used to set bounds to 1001
total = 1 #running total
current = 1 #current corner we land on
while size < 1001:
    size += 2
    for x in range(4): #each square has 4 corners
        current += (size - 1)
        total += current

print(total)