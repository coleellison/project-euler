#Project Euler Problem 39
#https://projecteuler.net/problem=39


def get_pythag(m, n):
    """
    Generates the sum of a relatively prime pythagorean triple using Euclid's formula
    Parameters
    ----------
    m : int
        first input
    n : TYPE
        second input

    Returns
    -------
    int
        sum of the three sides of the pythagorean triple
    """
    a = int(m ** 2 - n ** 2)
    b = int(2 * m * n)
    c = int(m ** 2 + n ** 2)
    return (a + b + c)

def coprime_check(a, b):
    """
    Parameters
    ----------
    a : int
        first input
    b : TYPE
        second input

    Returns
    -------
    bool
        returns True if a and b are coprime, else False
    """
    while b != 0:
        c = max(a, b) % min(a, b)
        a = min(a, b)
        b = c
    if a != 1:
        return False
    else:
        return True

def odd_even(a, b):
    """
    Parameters
    ----------
    a : int
        first input
    b : int
        second input

    Returns
    -------
    bool
        returns True if one term is odd and returns False if both or neither are.
    """
    if (a + b) % 2 == 1:
        return True
    else:
        return False


triple_sums = []

M = 2
while M < 500: #upper limit
    N = 1
    while N < M: #N cannot exceed M else side length would be negative
        if coprime_check(M, N) and odd_even(M, N):
            triple_sums.append(get_pythag(M, N))
        N += 1
    M += 1
triples = []
for i in triple_sums:
    if i < 1000: #upper limit
        triples.append(i)

best = [0, 0]
for i in range(1, 1001): #check for which numbers <= 1000 are divisible by the most triple sums
    n = 0
    for j in triples:
        if i % j == 0:
            n += 1
    if n > best[1]:
        best = [i, n] #i is the number, n is how many pythagorean sum factors it has

print(best[0])