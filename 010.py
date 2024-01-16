#Project Euler Problem 10
#projecteuler.net/problem=10

limit = 2000000 #maximum prime value

prime_list = [True] * limit #create a list of all True
prime_list[0] = False #base case 0 isn't prime
prime_list[1] = False #base case 1 isn't prime


#sieve of eratosthenes
for i in range(int(limit ** .5)): #we only need to check for factors under square root of our limit
    if prime_list[i] == True: #the index is a prime number
        for j in range(i ** 2, limit, i): #replace all multiples of the number, starting at i^2, with False
            prime_list[j] = False
#now our list has boolean values indicating whether each index is prime

total = 0

for i in range(limit):
    if prime_list[i]: #add the index to the sum if it is prime
        total += i

print(total)
