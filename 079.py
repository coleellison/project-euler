#Project Euler Problem 79
#https://projecteuler.net/problem=79

from itertools import permutations

rawinp = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""

#Digits 4 and 5 do not show up in the input
#Additionally, no number shows up twice
inp = [[i for i in x] for x in rawinp.split("\n")]

perms = ["".join([str(x) for x in i]) for i in permutations([1,2,3,6,7,8,9,0],8)] #Only use necessary digits
for perm in perms:
    success = True
    for order in inp:
        if perm.index(order[0]) > perm.index(order[1]):
            success = False
            break
        if perm.index(order[1]) > perm.index(order[2]):
            success = False
            break
    if success:
        print(int(perm))
        exit()
