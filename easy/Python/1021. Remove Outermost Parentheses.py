#Date:
#Question:
#Input:

#Output: "()()()"
#Explanation: 
#The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
#After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
#Type: Easy


#Thoughts:
#Thought through while driving to my sister's.
#since we always have an open and close bracket,
#what we first need to do is check how many open bracket ( there is,
#and since we need to take out the most outer ones,
#when we check our 'count' later, we will start our if statment at the second (
#and add to the string.
# since our first if statement check if the string is (, our else statement will be ),
# and everytime it produced and ), count will -1 and end until 0 and continue looping
# till the end.

((()))

def removeOuterParentheses(s):
    count = 0 #count the number of '('
    output = '' #our output
    for item in s:
        if item == '(':
            count += 1
            print(count)
            if count > 1:
                output += item
        else:
            count -= 1
            if count > 0:
                output +=item
    return output

s = "(()())(())"

print(removeOuterParentheses(s))

#Runtime: 44 ms, faster than 27.62% of Python3 online submissions for Remove Outermost Parentheses.
#Memory Usage: 14.7 MB, less than 8.61% of Python3 online submissions for Remove Outermost Parentheses.
#08/07/2021 17:10	Accepted	44 ms	14.7 MB	python3
