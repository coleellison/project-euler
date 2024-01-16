#Project Euler Problem 18
#https://projecteuler.net/problem=18

"""
Note: This solution uses brute force due to the small size of the triangle.
For an optimized solution, see 67.py
"""

df = [
      [75],
      [95, 64],
      [17, 47, 82],
      [18, 35, 87, 10],
      [20,  4, 82, 47, 65],
      [19,  1, 23, 75,  3, 34],
      [88,  2, 77, 73,  7, 63, 67],
      [99, 65,  4, 28,  6, 16, 70, 92],
      [41, 41, 26, 56, 83, 40, 80, 70, 33],
      [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
      [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
      [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
      [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
      [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
      [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
      ]

def path_sum(num):
    """
    Parameters
    ----------
    num : int
        an integer from 0 to 2 ^ 14 - 1.
        this integer will define the path we take through the triangular 2 dimensional array

    Returns
    -------
    total : int
        the sum of each item along the path we took
    """
    i = 0 #start at the top left
    j = 0
    total = 0
    while j < 15:
        total += df[j][i] #add the number we landed on
        i += num % 2 #if our number is odd, move one to the right
        j += 1 #move to the next row
        num //= 2 #divide the number by 2. this new number will form our index for the next iteration.
    return total

best = 0
path = 0
while path < 2 ** 14 - 1:
    best = max(best, path_sum(path)) #record our new best path as we come across one
    path += 1 #increase our path seed by 1

print(best)