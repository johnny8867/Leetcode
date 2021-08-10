#Date:080821
#Question:
#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

#Type: Easy


#Thoughts:
#using while loop and use remove function to remove it
#or we can create a loop and if item != val, append.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


#08/08/2021 21:51	Accepted	36 ms	14.1 MB	python3
