#Date:08152021
#Question:
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Type: Easy


#Thoughts:
# I did a similar question before.... but yeah using set() will make the list distinct,
#and then just compare size of original string to the distinct one
#simple as that :D

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else:
            return False


#Runtime: 120 ms, faster than 60.03% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 20 MB, less than 78.80% of Python3 online submissions for Contains Duplicate.
#08/16/2021 21:19	Accepted	120 ms	20 MB	python3
