#Date:081521
#Question:Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#Input: columnNumber = 1
#Output: "A"

#Type: Easy


#Thoughts:
#write out the calculation to know the algorithm... not too sure why -1 first,
#and we can see that the mod number is the according number, and import string to convert it,
#and since the mod number is backward... then use .reverse() to reverse the list.

import string

alphabet = string.ascii_uppercase


def convertToTitle(columnNumber):
    number = []
    while columnNumber >26:
        columnNumber -= 1 
        number.append(columnNumber % 26)
        columnNumber = columnNumber // 26
    else:
        columnNumber -= 1 
        number.append(columnNumber)
    print(number)
    word = ""
    number.reverse()
    for i in range (len(number)):
        word += alphabet[(number[i])]
    return word

print(convertToTitle(701))

#Runtime: 32 ms, faster than 45.56% of Python3 online submissions for Excel Sheet Column Title.
#Memory Usage: 14.2 MB, less than 71.84% of Python3 online submissions for Excel Sheet Column Title.
#08/15/2021 01:39	Accepted	32 ms	14.2 MB	python3
