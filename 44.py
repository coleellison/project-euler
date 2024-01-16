#Project Euler Problem 44
#https://projecteuler.net/problem=44

pent_list = [1]

def get_next_pent(lst): #appends new pent to input list
    """
    Parameters
    ----------
    lst
        input list
    """
    term_num = len(lst)
    new_term = lst[-1] + 3 * term_num + 1 #delta between terms is 3n + 1
    lst.append(new_term)

get_next_pent(pent_list)

sol = 0
while sol == 0:
    get_next_pent(pent_list)
    for pent_1 in pent_list:
        pent_2 = pent_list[-1] - pent_1
        if (pent_2 in pent_list and abs(pent_2 - pent_1) in pent_list): #check criteria
            sol = abs(pent_2 - pent_1)
            break #end loop after first match

print(sol)
