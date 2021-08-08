#Date:
#Question:
#Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).


#Type: Easy


#Thoughts:
#first thought was that use a built in count, done. However, I think built in count 
#works in string only and I didn't konw there was a bin() function until I looked into the discussion
#the comment out method works in here but didn't pass the test in leetcode and I'm not sure why


class Solution:
    def hammingWeight(self, n: int) -> int:
#        num = 0
#        n = str(n)
#        for i in (n):
#            num += int(i)
#        return num
        return bin(n).count('1')


#Runtime: 32 ms, faster than 60.78% of Python3 online submissions for Number of 1 Bits.
#Memory Usage: 14.3 MB, less than 37.13% of Python3 online submissions for Number of 1 Bits.
#08/08/2021 16:42	Accepted	32 ms	14.3 MB	python3
