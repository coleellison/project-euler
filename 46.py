#Project Euler Problem 46
#https://projecteuler.net/problem=46

prime_list = [2, 3]

def prime_check(n): #checks if given number is prime
    """
    Parameters
    ----------
    n: int
        input

    Returns
    -------
    bool
        True if prime, False if not
    """
    for i in prime_list:
        if n % i == 0:
            return False
    return True

prime_list = [2, 3]
def get_next_prime(): #finds the next prime and appends to prime_list
    x = prime_list[-1]
    while True:
        x += 2
        if prime_check(x):
            prime_list.append(x)
            break

def double_square_check(x): #checks if given number is twice a square number
    """
    Parameters
    ----------
    x: int
        input number

    Returns
    -------
    bool
        True if twice a prime, False if not
    """
    x //= 2
    if int(x ** .5) ** 2 == x:
        return True
    else:
        return False


odd_composites = []
i = 3
while i < 10000:
    if i > prime_list[-1]:
        get_next_prime() #populates prime list
    if prime_list.count(i) == 0:
        odd_composites.append(i) #list of odd composite integers
    i += 2

for i in odd_composites:
    count = 0 #flag to check condition
    for j in prime_list[1:]:
        if i > j:
            if double_square_check(i - j): #check if the difference between the odd composite and each prime under it is double a square
                count += 1
                break
    if count == 0:
        print(i) #print first instance, then end loop
        break