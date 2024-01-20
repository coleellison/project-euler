#Project Euler Problem 61
#https://projecteuler.net/problem=61

from itertools import permutations

#generate nth n-gon number
triangle = lambda n: (n) * (n + 1) // 2
square = lambda n: (n) ** 2
pentagon = lambda n: (n) * (3 * n - 1) // 2
hexagon = lambda n: (n) * (2 * n - 1)
heptagon = lambda n: (n) * (5 * n - 3) // 2
octagon = lambda n: (n) * (3 * n - 2)

#lists of n-gon numbers
list3 = []
i = 1
while triangle(i) < 10000:
    if triangle(i) >= 1000:
        list3.append(str(triangle(i)))
    i += 1
list4 = []
i = 1
while square(i) < 10000:
    if square(i) >= 1000:
        list4.append(str(square(i)))
    i += 1
list5 = []
i = 1
while pentagon(i) < 10000:
    if pentagon(i) >= 1000:
        list5.append(str(pentagon(i)))
    i += 1
list6 = []
i = 1
while hexagon(i) < 10000:
    if hexagon(i) >= 1000:
        list6.append(str(hexagon(i)))
    i += 1
list7 = []
i = 1
while heptagon(i) < 10000:
    if heptagon(i) >= 1000:
        list7.append(str(heptagon(i)))
    i += 1
list8 = []
i = 1
while octagon(i) < 10000:
    if octagon(i) >= 1000:
        list8.append(str(octagon(i)))
    i += 1

#array of n-gon numbers
nums = [list3,list4,list5,list6,list7,list8]

#check all ways to order the numbers
orderings = [i for i in permutations(range(6), 6)]
end = False
for x in range(len(orderings)):
    order = orderings[x]               
    for i in nums[order[0]]:
        for j in nums[order[1]]:
            for k in nums[order[2]]:
                a = i[2:] + j[:2] #first two digits of the first + last two digits of the second
                b = j[2:] + k[:2]
                c = k[2:] + i[:2]
                if a in nums[order[3]]: #check if it's a valid concatenation in the remaining lists
                    if b in nums[order[4]]:
                        if c in nums[order[5]]:
                            print(sum([int(n) for n in [i,j,k,a,b,c]])) #sum them
                            exit()