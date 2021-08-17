#Date:081621
#Question: 231
#Given an integer n, return true if it is a power of two. Otherwise, return false.

#An integer n is a power of two, if there exists an integer x such that n == 2x.


#Type: Easy


#Thoughts:
#I honestly thought about recursion at first... but I don't think it's efficiency enough
#then I went to discussion LOL

#then I saw discussion about & operator, and I'm like oh my this is actually really smart
# so & is 'AND' operation, but it's done in bits
#and we learned in 2DI4, we know that all 2 to the power of x will be in form of
# 1000, 10000000000, 1000000, so we can use if n & n-1 ==0, then it's 2^x
# 0111, 01111111111, 0111111
# and we also have to make sure the n is greater than 0.
#after understand the algo, it's pretty simple and straight forward!

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and (n & n-1) == 0:
            return True
        else:
            return False

#Runtime: 24 ms, faster than 96.77% of Python3 online submissions for Power of Two.
#Memory Usage: 14.2 MB, less than 69.36% of Python3 online submissions for Power of Two.
#08/16/2021 23:05	Accepted	24 ms	14.2 MB	python3
