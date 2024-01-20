#Project Euler Problem 57
#https://projecteuler.net/problem=57


#denominator defined recursively: d(x) = 2 * d(x-1) + d(x-2)
#numerator defined by denominator: n(x) = d(x) + d(x-1)

sequence = [1, 2]
for i in range(1000): #create denominators
    new_term = 2 * sequence[-1] + sequence[-2]
    sequence.append(new_term)

total = 0
for i in range(1,len(sequence)):
    numerator = str(sequence[i] + sequence[i - 1])
    denominator = str(sequence[i])
    if len(numerator) > len(denominator): #numerator has more digits
        total += 1

print(total)