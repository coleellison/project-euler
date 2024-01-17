#Project Euler Problem 38
#https://projecteuler.net/problem=38

target = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #pandigital condition to be met

best_string = ""
for num in range(10000): #the number cannot be more than 5 digits
    pan_string = ""
    i = 1
    while len(pan_string) < 9: #cuts off when we meet or go over
        temp_num = num * i
        pan_string += str(temp_num) #append the new multiple
        i += 1
    if sorted(pan_string) != target: #check against target
        continue #continue on to next num
    if (len(pan_string) == 9) and (pan_string > best_string): #check for the best product
        best_string = pan_string

print(int(best_string))
