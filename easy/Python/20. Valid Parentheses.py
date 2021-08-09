#Date:080821
#Question:
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.


#Type: Easy


#Thoughts:

#Didn't thought of this... but I think this method is actually pretty smart...
#Think it like tetris, if (),{},[] are together, remove them,
#and if length = 0 at the end, return true, else return false.

class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
        if len(s) != 0:
            return False
        else:
            return True
        
            
#Runtime: 36 ms, faster than 20.43% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 14.4 MB, less than 35.15% of Python3 online submissions for Valid Parentheses.
#08/08/2021 20:22	Accepted	36 ms	14.4 MB	python3
