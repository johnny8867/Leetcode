#Date:081621
#Question:
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#Type: Easy


#Thoughts:
#ummmmmmmm.... use sorted to sort the string and compare..?
#this question look like a trap but it's not LOL


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

#Runtime: 48 ms, faster than 68.07% of Python3 online submissions for Valid Anagram.
#Memory Usage: 14.8 MB, less than 30.80% of Python3 online submissions for Valid Anagram.
#08/16/2021 23:15	Accepted	48 ms	14.8 MB	python3
