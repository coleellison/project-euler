#Project Euler Problem 49
#https://projecteuler.net/problem=49

prime_list = [2]
i = 3

while i < 10000: #generate prime list
    count = 0
    for j in prime_list:
        if i % j == 0:
            count += 1
            break
    if count == 0:
        prime_list.append(i)
    i += 2

four_digit_primes = []

for i in prime_list: #filter for 4-digit primes
    if i > 1000:
        four_digit_primes.append(i)


digit_list = []
for i in four_digit_primes: #create tuples of sorted and unsorted numbers
    num_str = "".join(sorted(str(i)))
    digit_list.append((num_str, i))

digit_list.sort() #sort them, placing permutations adjacent

triplets = []

for i in range(len(digit_list) - 2):
    if digit_list[i][0] == digit_list[i + 1][0] and digit_list[i][0] == digit_list[i + 2][0]: #sorted values are the same
        triplet = [digit_list[i][1], digit_list[i + 1][1], digit_list[i + 2][1]] #list of strings
        triplets.append(triplet)

for i in triplets:
    if i[2] - i[1] == i[1] - i[0]: #distance is the same
        print(str(i[0])+str(i[1])+str(i[2])) #print concatenation
        
