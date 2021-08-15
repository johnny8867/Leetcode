#Date:081521
#Question:
#Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

#For example:

#A -> 1
#B -> 2
#C -> 3
#...
#Z -> 26
#AA -> 27
#AB -> 28 
#...
#Type: Easy

#Thoughts:
#if don't understand the pattern, write it out,
#I can see that for double digit it's *26 (for example given AA = 26+1)
#and AAA ->26*26*1 +26*1 + 1 => 703
#and I found ord() built in function, it converts string to ascii number, and - the origin point, which is 'A', and + 1 for A


def titleToNumber(columnTitle):
    number = 0
    for item in columnTitle:
        number = number * 26 + ord(item) - ord('A') + 1
            
    return number
print(titleToNumber('AAA'))

#Runtime: 46 ms, faster than 5.96% of Python3 online submissions for Excel Sheet Column Number.
#Memory Usage: 14.2 MB, less than 73.52% of Python3 online submissions for Excel Sheet Column Number.
#08/15/2021 00:36	Accepted	46 ms	14.2 MB	python3
