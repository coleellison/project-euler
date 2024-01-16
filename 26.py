#Project Euler Problem 26
#https://projecteuler.net/problem=26

def digit_count(x):
    """
    Parameters
    ----------
    x : int
        input we are checking

    Returns
    -------
    num : int
        the number of repeating digits in 1/x
    """
    i = 9
    num = 1
    while x % 2 == 0: #remove multiples of 2
        x = x // 2
    while x % 5 == 0: #remove multiples of 5
        x = x // 5
    while i % x != 0: #if x doesn't go into 9, try 99, then 999, etc.
        i = i * 10 + 9
        num += 1
    return num #the number of 9 digits in the smallest multiple of x is the number of digits 1/x it takes to repeat

d = 1
digit_dict = {}
longest = 1
max_digits = 1

while d < 1000:
    if digit_count(d) > max_digits: #new record
        max_digits = digit_count(d) #set max_digits to continue checking
        longest = d #record the value of which value has the longest repeating decimal
    d += 1

print(longest)