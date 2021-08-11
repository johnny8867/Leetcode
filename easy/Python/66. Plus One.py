#Date:081021
#Question:
#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.

#Type: Easy


#Thoughts:
#Because we know it's not going to be empty for sure...
#we can either do recursion as what if we need to create more digit like 99 -> 100
#Or just use the cheating method... convert to one whole string, convert to int and add then convert to string
#again, and break it into individual character. and return


digits = [999]
word = ""
numbers = []
for item in digits:
    word += str(item)
word = int(word)+1
word = str(word)
for i in range(len(word)):
    numbers.append(int(word[i]))
print(numbers)


#Your runtime beats 27.67 % of python3 submissions.
#08/10/2021 21:19	Accepted	36 ms	14 MB	python3
