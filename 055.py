#Project Euler Problem 55
#https://projecteuler.net/problem=55

def is_lychrel(num):
    #checks if a number is lychrel (up to 50 iterations)
    for i in range(50):
        num += int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            return False
    return True

total = 0
for i in range(10000):
    if is_lychrel(i):
        total += 1

print(total)