#Project Euler Problem 65
#https://projecteuler.net/problem=65

e = [2] #list representation of e
for i in range(1,34): #follow pattern of e's continued fraction to 100 places
    e.append(1)
    e.append(2 * i)
    e.append(1)

def convergent(maxindex):
    #generate the fraction representation of continued fraction up to maxindex
    cvg = e[:maxindex]
    frac = [1, cvg[-1]]
    while len(cvg) > 1:
        cvg.pop(-1)
        frac[0] += frac[-1] * cvg[-1]
        frac.reverse()
    frac.reverse()
    return frac

cvg100 = convergent(100)
num = cvg100[0]
total = 0
for i in str(num): #sum the digits
    total += int(i)

print(total)
