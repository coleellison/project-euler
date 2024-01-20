#Project Euler Problem 62
#https://projecteuler.net/problem=62

cube_dict = {}
i = 0
while True:
    perm_list = sorted(str(i ** 3))
    perm = ""
    for char in perm_list:
        perm += char
    if perm not in cube_dict:
        cube_dict[perm] = [i ** 3] #construct a list of permutations resulting in perfect cubes
    else:
        cube_dict[perm] += [i ** 3] #add onto the entry if it already exists
    if len(cube_dict[perm]) == 5: #if there are five permutations constructed
        print(min(cube_dict[perm])) #choose the smallest
        exit()
    i += 1