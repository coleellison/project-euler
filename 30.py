#Project Euler Problem 30
#https://projecteuler.net/problem=30

#6 * (9 ** 5) = 354294 < 999999.
#No 7 digit numbers can be written as the sum of their digits' fifth powers.
#We can set an upper limit of 10 ** 6

total = 0
for x in range(10, 1000000):
    digit_sum = 0
    for char in str(x): #Use a string for easier digit iteration
        digit_sum += int(char) ** 5 #Convert back to int for operations
    if digit_sum == x:
        total += x

print(total)
        