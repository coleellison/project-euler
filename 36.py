#Project Euler Problem 36
#https://projecteuler.net/problem=36

palindromes_10 = []
def is_palindrome(num):
    """
    Parameters
    ----------
    num : int
        input number

    Returns
    -------
    bool
        returns True if num is a palindrome
    """
    num_str = str(num)
    count = 0
    for i in range(len(num_str)):
        if num_str[i] != num_str[-(i + 1)]:
            count += 1
    if count == 0:
        return True

def decimal_to_binary(num): #wrote my own conversion functions for fun :)
    """
    Parameters
    ----------
    num : int
        input base 10 number

    Returns
    -------
    binary : int
        num converted to binary
    """
    temp_string = ""
    while num > 0:
        temp_string = str(num % 2) + temp_string
        num //= 2
    binary = int(temp_string)
    return binary

def binary_to_decimal(num):
    """
    Parameters
    ----------
    num : int
        input binary number

    Returns
    -------
    decimal : int
        num converted to decimal
    """
    decimal = 0
    temp_string = str(num)
    reversed_string = ""
    for i in range(1, len(temp_string) + 1):
        reversed_string += temp_string[-i]
    for i in range(len(reversed_string)):
        decimal += int(reversed_string[i]) * (2 ** i)
    return decimal
        


for i in range(1, 1000000): #check all numbers under 1 million
    if is_palindrome(i) == True:
        palindromes_10.append(i) #create a list of palindromes

pali_binary = []
for i in palindromes_10: 
    pali_binary.append(decimal_to_binary(i)) #convert list to binary

double_palis = []

for i in pali_binary:
    if is_palindrome(i) == True: #check our decimal palindromes to see if they are also binary palindromes
        double_palis.append(i)

total = 0

for i in double_palis:
    total += binary_to_decimal(i) #convert back to decimal and add to total
    
print(total)