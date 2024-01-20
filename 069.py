#Project Euler Problem 69
#https://projecteuler.net/problem=69

def list_product(input_list):
    #product of all elements in a list
    product = 1
    for i in input_list:
        product *= i
    return product

def is_prime(n):
    #primality test
    prime = True
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

prime_list = [2] #we want to maximize the amount of prime numbers whose product is under 1000000
while list_product(prime_list) <= 1000000:
    n = prime_list[-1] + 1
    while not is_prime(n): #go until you get the next prime
        n += 1
    prime_list.append(n)

print(list_product(prime_list[:-1])) #ignore the last element

