#Project Euler Problem 20
#https://projecteuler.net/problem=20

def factorial(N):
    """
    Parameters
    ----------
    N : int
        the number we will calculate the factorial of

    Returns
    -------
    ans : int
        N factorial
    """
    ans = 1
    for i in range(1, N + 1):
        ans *= i #multiply each number between 1 and N
    return ans

print(sum(int(i) for i in str(factorial(100))))
