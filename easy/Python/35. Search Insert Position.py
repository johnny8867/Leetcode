#Date:
#Question:
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


#Type: Easy


#Thoughts:

#So we have to think of 3 condition, number inside the list > < and = to our target number
# = or > is simple, it will just be position i in the list
# and less than, will just means that we need to index additional position to the list,
# meaning that it will need +1
#such a simple question but took me 8th submission LOL
#meaning it's time for bed.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return i+1

#Runtime: 44 ms, faster than 90.67% of Python3 online submissions for Search Insert Position.
#Memory Usage: 15.1 MB, less than 55.30% of Python3 online submissions for Search Insert Position.
#08/10/2021 00:52	Accepted	44 ms	15.1 MB	python3
