#Project Euler Problem 17
#https://projecteuler.net/problem=17

nums_100 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
words_100 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine', 'forty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three', 'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty', 'sixty-one', 'sixty-two', 'sixty-three', 'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven', 'sixty-eight', 'sixty-nine', 'seventy', 'seventy-one', 'seventy-two', 'seventy-three', 'seventy-four', 'seventy-five', 'seventy-six', 'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty', 'eighty-one', 'eighty-two', 'eighty-three', 'eighty-four', 'eighty-five', 'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety', 'ninety-one', 'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven', 'ninety-eight', 'ninety-nine']
dict_100 = dict()
for i in range(100):
    dict_100.update({nums_100[i]: words_100[i]}) #combine the elements of each string into a dictionary

def get_word(num):
    """
    Parameters
    ----------
    num : int
        a number between 1 and 1000

    Returns
    -------
    word : str
        the num returned as a string
    """
    if num < 100:
        word = str(dict_100[num]) #return the number if it is less than 100
    elif num % 100 == 0:
        word = str(dict_100[num // 100]) + " hundred" #add hundred on to the number if it is divisible by 100
    else:
        word = str(dict_100[num // 100])+" hundred and " + str(dict_100[num % 100]) #otherwise, construct the number by its hundred and tens+ones place
    return word



thousand_list = []
i = 0

while i < 1000:
    thousand_list.append(get_word(i)) #add all words from 1 to 1000 to the list
    i += 1
thousand_list.append("one thousand") #add the special case (1000 itself)

alphabet_list = []
for x in thousand_list:
    alphabet_word = x.replace(" ", "") #remove spaces
    alphabet_word = alphabet_word.replace("-", "") #remove hyphens
    alphabet_list.append(alphabet_word)

char_num = 0
for x in alphabet_list:
    char_num += len(x) #add the lengths of each number to the total
print(char_num)
