#Date:080821
#Question:
#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


#Type: Easy


#Thoughts:
#if negative, return false
#and write another variable that converts to string and backward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = str(x)
        y = (y[::-1])
        if int(y) == x:
            return True

#Runtime: 56 ms, faster than 78.90% of Python3 online submissions for Palindrome Number.
#Memory Usage: 13.9 MB, less than 99.96% of Python3 online submissions for Palindrome Number.
#08/08/2021 19:23	Accepted	56 ms	13.9 MB	python3
