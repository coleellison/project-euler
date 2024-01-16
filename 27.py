#Project Euler Problem 27
#https://projecteuler.net/problem=27


#We know b must be a prime less than 1000. Otherwise, initial condition n = 0 would fail
prime_1000 = [2]
num = 3
while num < 1000: #Find all primes under 1000
    count = 0
    for i in prime_1000:
        if num % i == 0:
            count += 1
            break
    if count == 0:
        prime_1000.append(num)
    num += 2

#We can set an upper limit of the product n ** 2 + n * a + b to speed up our search
prime_list = [2]
num = 3
while num < 100000:
    count = 0
    for i in prime_list:
        if num % i == 0:
            count += 1
            break
    if count == 0:
        prime_list.append(num)
    num += 2

iter_list = []

#We can exhaustively search for values of a
for b in prime_1000:
    a = b * -1
    while a < 1000:
        n = 0
        while (n ** 2 + n * a + b) in prime_list: #Go until the expression is no longer prime
            n += 1
        temp_list = [n, a, b]
        iter_list.append(temp_list)
        a += 1

iter_list.sort() #Sorts by n, listing the longest sequence last

print(iter_list[-1][1] * iter_list[-1][2]) #a * b
        
    