#Project Euler Problem 21
#https://projecteuler.net/problem=21

def divisor_sum(N):
    """
    Parameters
    ----------
    N : int
        number to be factored

    Returns
    -------
    div_sum : int
        the sum of proper divisors of N
    """
    i = 1
    div_sum = 0
    while i < N:
        if N % i == 0: #if the divisor divides N evenly
            div_sum += i #add the proper divisor to the total
        i += 1
    return div_sum


div_list = []
for i in range(10000): #check under 10000
    div_list.append(divisor_sum(i)) #generates list of the sum of proper divisors for N

amicable_sum = 0
for i in range(10000):
    if div_list[i] < 10000: #ensures that there are no index errors
        if (i == div_list[div_list[i]] and i != div_list[i]): #check if the numbers are amicable
            amicable_sum += i

print(amicable_sum)