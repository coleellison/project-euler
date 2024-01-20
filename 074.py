#Project Euler Problem 74
#https://projecteuler.net/problem=74

def factorial(n):
    #n factorial
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


def digit_factorial(n):
    #calculates the sum of factorials of each digit
    n = str(n)
    ans = 0
    for char in n:
        ans += factorial(int(char))
    return ans

def chain_length(n):
    #calculates the period before the chain repeats
    current = digit_factorial(n)
    chain = [n]
    while current not in chain: #loop exists once we have a repeat
        chain.append(current)
        current = digit_factorial(current)
    return len(chain)

total = 0
for i in range(1, 1000000):
    if chain_length(i) == 60: #desired specification
        total += 1
print(total)