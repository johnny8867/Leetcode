#Date: Aug 07, 2021
#Question:

#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.
#Type: Easy

#Thoughts:
#Because we want to compute the max number, so meaning that
#negative number doesn't help us, so we have a initial max number of
#nums[0], as our starting point and as we loop through nums, we will have a
#variable called current number, computing number of current, and if it's a negative number
#it will be put back to 0 and go to the next number in list.
#if it's not negative, it'll add the next number, and if it's > 0, it will compare with
#max number and continue to loop through next number and sum it, if > 0, continue, if it's <0
# then reset back to 0 and previous max number was stored. and pattern goes on till end of loop.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        current = 0
        
        for n in nums:
            if current < 0:
                current = 0
            current +=n
            max_num  = max(max_num, current)
        return max_num


#https://www.youtube.com/watch?v=5WZl3MMT0Eg&ab_channel=NeetCode

#Runtime: 64 ms, faster than 75.89% of Python3 online submissions for Maximum Subarray.
#Memory Usage: 15.1 MB, less than 21.31% of Python3 online submissions for Maximum Subarray.
#08/07/2021 15:22	Accepted	64 ms	15.1 MB	python3

#Update

#if we change built in function of max() ->
    #if max_num <current:
    #           max_num = current

#resubmit

#Runtime: 56 ms, faster than 97.48% of Python3 online submissions for Maximum Subarray.
#Memory Usage: 15 MB, less than 85.39% of Python3 online submissions for Maximum Subarray.
#08/07/2021 15:29	Accepted	56 ms	15 MB	python3
