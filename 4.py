#Project Euler Problem 4
#https://projecteuler.net/problem=4

i = 999999

def factorcheck(Palindrome):
    """
    Parameters
    ----------
    Palindrome : integer
        derives factors of the given palindrome
        checks for factors less than the square root
        appends the factor to the list of factors

    Returns
    -------
    bool
        if the greatest factor less than the square root is 3 digits, so is its compliment (for 6 digit numbers)
        returns True if the last factor is 3 digit
        returns False if the last factor is not 3 digit.
    """
    factorlist = []
    a = 1
    while a < (Palindrome ** .5):
        if Palindrome % a == 0:
            factorlist.append(a)
            factorlist.append(int(Palindrome / a))
            a += 1
        else:
            a += 1
    if len(str(factorlist[-1])) == 3:
        return True
    else:
        return False

while True: #infinite loop, break when case is found
    stri = str(i) #convert integer to string to check if it is a palindrome
    if (stri[0] == stri[-1] and stri[1] == stri[-2] and stri[2] == stri[-3]): #checks if a 5 or 6 digit number is a palindrome
        if factorcheck(i): #evaluates to True if it has a pair of 3 digit factors
            print(i)
            break
    i -= 1 #count down from 999999 to ensure we get the largest palindrome which meets criteria