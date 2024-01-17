#Project Euler Problem 3
#https://projecteuler.net/problem=3

n = 600851475143 #input
i = 2 #base case
factors = []
while i < n:
    if n % i == 0: #checks for divisibility
        n //= i #divides n by the factor
        factors.append(i)
    else:
        i += 1 #only increment when the number is not divisible. ensures we get the full prime factorization.

print(i) #the while loop breaks when i = n, so n is the greatest prime factor.
