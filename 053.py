#Project Euler Problem 53
#https://projecteuler.net/problem=53

def factorial(N):
    """

    Parameters
    ----------
    N : int
        input

    Returns
    -------
    int
        N factorial
    """
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

def combination(N, R):
    """

    Parameters
    ----------
    N : int
        left of combination
    R : int
        right of combination

    Returns
    -------
    int
        N choose R
    """
    return (factorial(N)) / (factorial(R) * factorial(N - R))

total = 0

for n in range(1, 101): #simple brute force. computers are good at math :)
    for r in range(n):
        if combination(n, r) > 10 ** 6:
            total += 1

print(total)