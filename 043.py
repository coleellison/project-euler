#Project Euler Problem 43
#https://projecteuler.net/problem=43

def div_list(num):
    """
    Parameters
    ----------
    num : int
        input number

    Returns
    -------
    result: list
        list of 3 digit strings of numbers divisble by num
    """
    result = []
    for i in range(1000):
        if i % num == 0:
            temp_str = str(i)
            if len(temp_str) < 3: #ensure string is length 3
                    temp_str = "0" + temp_str
            if len(temp_str) < 3:
                    temp_str = "0" + temp_str
            result.append(temp_str)
    
    
    return result

div_1 = div_list(2)
div_2 = div_list(3)
div_3 = div_list(5)
div_4 = div_list(7)
div_5 = div_list(11)
div_6 = div_list(13)
div_7 = div_list(17)

#sequentially filter through  candidates
candidates_1 = [] #divisble by 2 and 3
for i in div_1:
    for j in div_2:
        if i[-2] == j[0] and i[-1] == j[1] and j[2]:
            candidates_1.append(i + j[2])
            
candidates_2 = [] #divisible by 5
for i in candidates_1:
    for j in div_3:
        if i[-2] == j[0] and i[-1] == j[1] and j[2]:
            candidates_2.append(i + j[2])

candidates_3 = [] #divisible by 7
for i in candidates_2:
    for j in div_4:
        if i[-2] == j[0] and i[-1] == j[1] and j[2]:
            candidates_3.append(i + j[2])

candidates_4 = [] #divisible by 11
for i in candidates_3:
    for j in div_5:
        if i[-2] == j[0] and i[-1] == j[1] and j[2]:
            candidates_4.append(i + j[2])

candidates_5 = [] #divisible by 13
for i in candidates_4:
    for j in div_6:
        if i[-2] == j[0] and i[-1] == j[1] and j[2]:
            candidates_5.append(i + j[2])

candidates_6 = [] #divisible by 17
for i in candidates_5:
    for j in div_7:
        if i[-2] == j[0] and i[-1] == j[1] and j[2]:
            candidates_6.append(i + j[2])


valid_strings = []

for cand in candidates_6: #avoid duplicates
    dupe = 0
    temp_str = "".join(sorted(cand))
    for i in range(8):
        if temp_str[i] == temp_str[i + 1]:
            dupe += 1
            break
    if dupe == 0:
        valid_strings.append(cand)

solution_list = []

for i in valid_strings:
    for num in range(10):
        if str(num) not in i:
            solution_list.append(int(str(num) + i)) #fill in possible last digit

print(sum(solution_list))
    
