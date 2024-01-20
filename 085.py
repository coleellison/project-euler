#Project Euler Problem 85
#https://projecteuler.net/problem=85

n = 2000000
biggest = int((2 * n) ** .5) + 1 #otherwise we will exceed n

def num_rectangles(x,y):
    #calculates the number of rectanges that can be constructed within an x by y grid
    total = 0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            total += i * j
    return total

close = [(abs(n - num_rectangles(1, biggest)), biggest)] #use absolute value to find the minimum delta

for i in range(1, biggest + 1): #iterate over our x dimension
    j = 2
    while True:
        if num_rectangles(i,j) > n:
            close.append((abs(n - num_rectangles(i,j)), i * j)) #sort by delta, store area in tuple alongside it
            close.append((abs(n - num_rectangles(i,j - 1)), i * (j - 1)))
            break
        j += 1 #increment y dimension until we exceed n. then the last two are the two closest values (one an underestimate, the other an overestimate)

print(min(close)[1])