#Project Euler Problem 34
#https://projecteuler.net/problem=34

"""
If all digits are greater than 5, the number must end in 0.
However, if all digits are greater than 5, the number cannot end in 0.
To find an upper limit for our iteration, we can check two cases:
1: Last digit zero - We can set a generous upper limit of 5 million.
2: All digits less than 4 - These numbers are limited to be very small and will be covered within the above domain.
"""
def factorial(n):
    """
    Parameters
    ----------
    n : int
        the input number

    Returns
    -------
    product : int
        factorial of n
    """
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

num_sum = 0
for x in range(3, 5000000): #upper limit as explained above
    factorial_sum = 0
    for digit in str(x):
        factorial_sum += factorial(int(digit))
    if factorial_sum == x:
        num_sum += x

print(num_sum)
