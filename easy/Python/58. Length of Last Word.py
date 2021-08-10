#Date:081021
#Question:

#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.

#Type: Easy


#Thoughts:
#I had a good idea of what to do because I did a lot of similar things for string before.
#basically we can split the word by empty space, now we have a list, and now replace all the extra space with ''
#and now simply just return the length of last word, simple!


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        
        for item in words:
            item.replace(' ','')
        
        
        return len(words[-1])

#You are here!
#Your runtime beats 51.83 % of python3 submissions.
#08/10/2021 00:32	Accepted	32 ms	14.3 MB	python3
