#Project Euler Problem 6
#https://projecteuler.net/problem=6

n = 100
sqsum = ((n + 1) * (n) / 2) ** 2 #sum of sequence of natural numbers of 1 to n, squared

def sumsqfunc(x):
    """
    Parameters
    ----------
    x : int
        the maximum input to be squared then summed

    Returns
    -------
    total : int
        returns the sum total of numbers between 1 and x squared
    """
    
    i = 1
    total = 0
    while i <= x:
        total += i ** 2
        i += 1
    return total
sumsq = sumsqfunc(100) #apply function with input 100 according to the problem

difference = int(sqsum - sumsq)
print(difference)