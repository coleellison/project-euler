#Project Euler Problem 68
#https://projecteuler.net/problem=68

from itertools import permutations

def ringcheck(perm):
    """checks for a valid 5-gon ring

    Parameters
    ----------
    perm : list
        the ordering to populate the ring

    Returns
    -------
    False if the ring is invalid. The concatenation of digits if the ring meets all criteria.
    """
    legs = [(perm[4], perm[9], perm[5])]
    leg = perm[4] + perm[9] + perm[5]
    for i in range(4):
        if perm[i] + perm[i + 5] + perm[i + 6] != leg:
            return False
        legs.append((perm[i] , perm[i + 5] , perm[i + 6]))
    legs = sorted(legs, reverse=True)
    legs = (legs[-1], legs[0], legs[1], legs[2], legs[3])
    sol = ""
    for i in range(5):
        sol += "".join([str(x) for x in legs[i]])
    return sol
validstrings = []
inp = [i for i in permutations([9,8,7,6,5,4,3,2,1,10])] #starting with this ordering will test the highest value permutations first
for perm in inp:
    if perm.index(10) > 3: #problem criteria
        continue
    perm = list(perm)
    if ringcheck(perm):
        validstrings.append(ringcheck(perm))

validstrings.sort() #order the rings by concatenation value
print(validstrings[-1]) #select the highest value