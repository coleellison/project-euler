#Project Euler Problem 24
#https://projecteuler.net/problem=24

def factorial(n):
    """
    Parameters
    ----------
    n : int
        input number

    Returns
    -------
    factorial : int
        returns factorial of n
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
"""
producing the smallest orderings requires changing the least significant digits (as far right as possible)
for example, the first 120 iterations only require changing the first 5 digits (since 120 is 5 factorial)
the nth smallest ordering can be found by figuring out which digits need to be reordered
we can do so using the for loop below:
"""

multiplicity_list = [] #write one million as a sum of multiples of factorials 0 through 9
n = 999999 #one millionth index
for x in range(10):
    multiplicity = n // factorial(9 - x) #count the multiplicity of the given factorial
    n = n % factorial(9 - x)  #reassign n with the remainder
    multiplicity_list.append(multiplicity) #append the multiplicity to the list

digits = [i for i in range(10)]
num = ""
for x in multiplicity_list:
    num += str(digits[x]) #add the digit corresponding to the factorial multiplicity
    del digits[x] #remove from the list of digits
#being able to calculate the nth ordering without needing to know the previous n-1 orderings greatly increases efficiency
print(num)
