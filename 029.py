#Project Euler Problem 29
#https://projecteuler.net/problem=29

#brute force is very fast
powers = []
for a in range(2,101):
    for b in range(2, 101):
        x = int(a ** b)
        if x not in powers: #Avoid duplicates
            powers.append(x)
print(len(powers))
