#Date:081021
#Question:
#Given two binary strings a and b, return their sum as a binary string.

#Type: Easy


#Thoughts:
#Honestly.... no thoughts LOL
#Then I looked into the Discussion, found out we can add number in a different base (honestly didn't know that it existed)
#then it's much simple now, add it in base 2 then output the number in base 2 format.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, base = 2)+ int(b, base =2))
        

#Runtime: 32 ms, faster than 74.75% of Python3 online submissions for Add Binary.
#Memory Usage: 14 MB, less than 99.00% of Python3 online submissions for Add Binary.
#08/10/2021 21:43	Accepted	32 ms	14 MB	python3
