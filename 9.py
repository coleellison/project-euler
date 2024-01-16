#Project Euler Problem 9
#https://projecteuler.net/problem=9

m = 2
n = 1
def pyfunc(M, N):
    """
    Parameters
    ----------
    M : int
        used in Euclid's formula for exhaustively finding relatively prime pythagorean triples
    N : int
        used in Euclid's formula for exhaustively finding relatively prime pythagorean triples

    Returns
    -------
    int
        if the sum of a, b, c divides 1000 evenly, return the product of a, b, c with the quotient and then multiply them.
        else, return 0 as a flag to know to try a new combination
    """
    a = M ** 2 - N ** 2
    b = 2 * M * N
    c = M ** 2 + N ** 2
    if 1000 % (a + b + c) == 0:
        return int((a * b * c) * (1000 / (a + b + c)) ** 3)
    else:
        return 0
while n < 19: #values for n and m exceeding 19, 20 would result in the sum of a,b,c exceeding the limit of 1000.
    while m < 20: #try all combinations under 19, 20
        if pyfunc(m, n) != 0: #condition is met!
            print(pyfunc(m, n))
            break
        else:
            m += 1
    n += 1
    m = n + 1 #ensures m > n. otherwise m^2 - n^2 would be negative. triangles can't have negative side lengths!