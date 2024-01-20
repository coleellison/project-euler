#Project Euler Problem 84
#https://projecteuler.net/problem=84

from random import randint

curr = 0

chestpos = [2,17,33]
chancepos = [7,22,36]

rollhist = [(1,2),(3,4),(5,6)]

def doublecheck(hist):
    """checks for three doubles

    Parameters
    ----------
    hist : list
        3 most recent rolls

    Returns
    -------
    bool
        True if 3 doubles, False otherwise
    """
    for i in hist:
        if i[0] != i[1]:
            return False
    return True

def roll(n):
    """rolls two n-sided dice

    Parameters
    ----------
    n : int
        number of sides of dice

    Returns
    -------
    tuple
        both dice values (kept separate to check for doubles)
    """
    d1 = randint(1,n)
    d2 = randint(1,n)
    return (d1,d2)

def chest(currpos):
    """simulates pulling a community chest card

    Parameters
    ----------
    currpos : int
        current square

    Returns
    -------
    int
        new square to land on
    """
    draw = randint(1,16)
    if draw == 1:
        return 0 #go
    elif draw == 2:
        return 10 #jail
    else:
        return currpos #stay where you are

def chance(currpos):
    draw = randint(1,16)
    if draw == 1:
        return 0 #go
    elif draw == 2:
        return 10 #jail
    elif draw == 3:
        return 11 #c1
    elif draw == 4:
        return 24 #e3
    elif draw == 5:
        return 39 #h2
    elif draw == 6:
        return 5 #r1
    elif (draw == 7 or draw == 8):
        currpos += 5
        currpos -= currpos % 10
        currpos += 5
        currpos = currpos % 40
        return currpos #next railroad
    elif draw == 9:
        if currpos < 12:
            currpos = 12
        elif currpos < 28:
            currpos = 28
        else:
            currpos = 12
        return currpos #next utility company
    elif draw == 10:
        currpos -= 3
        return currpos #back 3 spaces
    else:
        return currpos #stay where you are

def advance(position):
    currroll = roll(4)
    rollhist.append(currroll) #keep track of past 3 rolls to look for doubles
    rollhist.pop(0)
    if doublecheck(rollhist):
        return 10 #go to jail
    position += sum(currroll)
    position = position % 40
    if position == 30:
        return 10 #go to jail
    if position in chestpos:
        return chest(position) #pull a community chest card
    if position in chancepos:
        return chance(position) #pull a chance card
    return position


frequency = [[0,i] for i in range(40)] #to keep track of frequencies

for i in range(10000000): #takes about 10 seconds on my macbook. gives consistent results
    frequency[curr][0] += 1
    curr = advance(curr)

frequency = sorted(frequency, reverse=True)
sol = ""
for term in frequency[:3]: #3 most popular squares
    sol += str(term[1])
print(sol)