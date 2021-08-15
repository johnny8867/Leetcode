#Date:
#Question:
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

#Type: Easy


#Thoughts:
#honestly I thought of hash table... but that's going to be a pain to do...
#then looking at discussion, I found the XOR method, but really I don't think
#I'll remember the true table for XOR regularly
#And second method I found that make senses to me,
#use set to find the dup numbers, sum them up as you can't set(nums)*2,
#with that, - sum or nums, really cleaver and clean actually.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #return (sum(set(nums))*2 - sum(nums))
        result = 0
        for item in nums:
            result ^= item
        return result

#Runtime: 183 ms, faster than 23.86% of Python3 online submissions for Single Number.
#Memory Usage: 16.7 MB, less than 59.50% of Python3 online submissions for Single Number.


#08/12/2021 22:41	Accepted	183 ms	16.7 MB	python3
#08/12/2021 22:38	Accepted	244 ms	16.5 MB	python3
