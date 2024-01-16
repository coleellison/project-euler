#Project Euler Problem 33
#https://projecteuler.net/problem=33

def common_digit(num1, num2):
    """
    Parameters
    ----------
    num1 : int
        first input number
    num2 : int
        second input number

    Returns
    -------
    common_list : list
        DESCRIPTION.
    """
    set1 = set()
    set2 = set()
    for char in str(num1): #use sets to find intersection
        set1.add(char)
    for char in str(num2):
        set2.add(char)
    common_set = set1 & set2
    common_list = list(common_set)
    return common_list
    
def gcf(num1, num2):
    """
    Parameters
    ----------
    num1 : int
        first input number
    num2 : int
        second input number

    Returns
    -------
    gcf of two numbers : int
    """
    while num1 % num2 != 0:
        temp_a = min(num1, num2)
        temp_b = num1 % num2
        num1 = temp_a
        num2 = temp_b
    return min(num1, num2)
        

a = 10
num_product = 1
den_product = 1
for n in range(a + 1, 100): #must be two digit
        for d in range(n + 1, 100): #must be a proper fraction
            for x in common_digit(n, d):
                if n * int(str(d).replace(x, "", 1)) == d * int(str(n).replace(x, "", 1)): #use strings for easier digit manipulation
                    if x != "0":
                        num_product *= n
                        den_product *= d

print(den_product // (gcf(num_product, den_product))) #print desired solution format