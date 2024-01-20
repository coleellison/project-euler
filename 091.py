#Project Euler Problem 91
#https://projecteuler.net/problem=91

dot = lambda v1,v2: v1[0] * v2[0] + v1[1] * v2[1] #dot product of vectors in R^2

total = 0
for i in range(1,(51**2)): #all combinations of locations for initial vector
    a = (i // 51, i % 51) #separate into coordinates
    for j in range(1,i):
        b = (j // 51, j % 51) #b < a to avoid double counting
        c = (a[0] - b[0], a[1] - b[1]) #a - b vector subtraction
        if dot(a,b) == 0: #dot product == 0 -> perpendicular vectors (right triangle)
            total += 1
            continue #only need to find one right angle (triangles can't have more, and we wouldn't want to double count anyways)
        if dot(b,c) == 0:
            total += 1
            continue
        if dot(c,a) == 0:
            total += 1
print(total)