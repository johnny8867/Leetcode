#Date Aug 7, 2021
#Type: Easy
#Question:
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.



#Thoughts:

nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                print(i,j)

two_sum(nums,target)


#Runtime: 4056 ms, faster than 20.97% of Python3 online submissions for Two Sum.
#Memory Usage: 14.8 MB, less than 92.37% of Python3 online submissions for Two Sum.
#08/07/2021 14:27	Accepted	4056 ms	14.8 MB	python3
