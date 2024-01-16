#Project Euler Problem 12
#https://projecteuler.net/problem=12

def triangle(N):
    """
    Parameters
    ----------
    N : int
        index for which we will calculate the nth triangular number

    Returns
    -------
    trianglen: int
        the nth triangular number
    """
    
    trianglen = ((N) * (N + 1)) // 2
    return trianglen

def factor(N):
    """
    Parameters
    ----------
    N : int
        the triangular number we wish to factor
    
    checks for factors less than the square root of N
    
    every factor less than the square root of N will have a corresponding factor greater than N
    
    if the number is a perfect square, add one additional factor

    Returns
    -------
    factorcount : int
        the number of factors the number has
    """
    
    i = 1
    factorcount = 0
    while i < (N ** .5):
        if N % i == 0:
            factorcount += 2
        i += 1
    if int((N ** .5)) ** 2 == N:
        factorcount += 1
    return factorcount
n = 1
while True: #loop until we have a solution
    num = factor(triangle(n)) #find all factors of the given triangular number
    if num < 500: #insufficient factors => try next number
        n += 1
    else:
        break #exit the loop once we have sufficient factors

print(triangle(n))