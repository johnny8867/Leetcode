#Date:081021
#Question:
#Implement strStr().

#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Type: Easy


#Thoughts:
#first I guess write the corner case of if both input are empty, return 0,
#then write a loop to check, from 0 to len of big word - len of small word + 1
#if not understand, e.g hello and ll, we would only need to check it 4 time
#which is from h, e , l, l and that's 4.
#else it's not in haystack, so return -1



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" and haystack == "":
            return 0
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1

            

#Runtime: 44 ms, faster than 46.68% of Python3 online submissions for Implement strStr().
#Memory Usage: 14.3 MB, less than 82.22% of Python3 online submissions for Implement strStr().
#08/10/2021 20:48	Accepted	44 ms	14.3 MB	python3
