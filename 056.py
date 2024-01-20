#Project Euler Problem 56
#https://projecteuler.net/problem=56

digit_sum = lambda num: sum([int(i) for i in str(num)])

max_sum = 0
for a in range(100):
    for b in range(a + 1): #skip double counting
        max_sum = max(max_sum, digit_sum(a ** b))

print(max_sum)