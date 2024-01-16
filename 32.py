#Project Euler Problem 32
#https://projecteuler.net/problem=32


from math import isqrt
def factor_list(num):
    """
    Parameters
    ----------
    num : int
        input number

    Returns
    -------
    factors : list
        list of all factors of number
    """
    factors = []
    for i in range(1, isqrt(num) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    factors.sort()
    return factors

target = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pandigitals = set() #using a set ensures that no element is counted twice
for number in range(100000): #Any number greater than 5 digits cannot be written pandigitally with its multiplicand and multiplier
    for i in range(len(factor_list(number))):
        digits = str(factor_list(number)[i]) + str(factor_list(number)[-1 - i]) + str(number) #multiplicand-multiplier-product string
        digits = sorted(digits) #sort the string to check if it matches [1..9]
        if digits == target:
            pandigitals.add(number)

print(sum(pandigitals))