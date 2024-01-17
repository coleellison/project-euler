#Project Euler Problem 31
#https://projecteuler.net/problem=31

#nested for loops for each coin type
total = 0
for b in range(101): #Each range value is the maximum number of the given coin that can fit under 200
    for c in range(41):
        for d in range(21):
            for e in range(11):
                for f in range(5):
                    for g in range(3):
                        for h in range(2): #If the combination <= 200, we can fill the rest with 1c coins to complete the total.
                            if int(2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h) <= 200:
                                total += 1
print(total)
