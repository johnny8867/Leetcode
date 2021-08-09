#Date:080821
#Question:
#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".


#Type: Easy


#Thoughts:

#learned built in function zip, going to write about it in my ipad.
# then it's very simple with the zip function,
# check set if there's duplicates, if the length the 1, meaning all of the
# prefix are there, append it to a word
#done!
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        a = zip(*strs)
        for x in a:
            if len(set(x)) ==1:
                prefix += x[0]
            else:
                break
        return prefix
        

            
#Runtime: 36 ms, faster than 53.89% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 14.3 MB, less than 56.39% of Python3 online submissions for Longest Common Prefix.
#08/08/2021 19:46	Accepted	36 ms	14.3 MB	python3
