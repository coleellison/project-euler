#Project Euler Problem 14
#https://projecteuler.net/problem=14

def collatz(N):
    """
    Parameters
    ----------
    N : int
        number to be tested

    Returns
    -------
    list
        return a list containing two elements:
            ops: int, the number of steps it takes for the collatz sequence to converge to 1
            i: copy of N, the number which we are testing
    """
    i = N
    ops = 1
    while N != 1:
        if N % 2 == 1: #if the number is odd
            N = N * 3 + 1 #perform the odd operation
            ops += 1
        else:
            N = N // 2 #otherwise the number is even, divide the number by 2
            ops += 1
    return [ops, i]

record = [0, 0]
num = 1
while num < 1000000:
    if collatz(num) > record: #if the term's collatz sequence has the most operations
        record = collatz(num) #update the record for longest collatz sequence
    num += 1

print(record[1]) #index 1 indicates the number for which the collatz sequence is longest