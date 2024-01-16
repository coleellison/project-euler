#Project Euler Problem 15
#https://projecteuler.net/problem=15

"""
It will always take 20 downs and 20 rights, for a total of 40.
These can be arranged in any order.
Answer = 40 choose 20
Generalized solution for any size grid:
"""    
n = 20

def factorial(X):
    """
    Parameters
    ----------
    X : int
        the integer input

    Returns
    -------
    result : int
        returns the factorial of our input X
    """
    i = 1
    result = 1
    while i <= X:
        result *= i #multiply each sequential number to the total
        i += 1
    return result

def ncr(N, R):
    """
    Parameters
    ----------
    N : int
        the total number of items we can select from
    R : int
        the number of items we select

    Returns
    -------
    result : int
        the number of ways to select R items from N options
    """
    result = int(factorial(N) / (factorial(R) * factorial(N - R))) #combination formula
    return result

paths = ncr((2 * n), n) #calculate number of paths
print(paths)
