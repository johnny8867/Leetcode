#Date:080821
#I'm not good with binary search tree
#Question:
#Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

#Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

#The tests are generated such that there is exactly one solution. You may not use the same element twice.

#Type: Easy


#Thoughts:
#since the list is in order list, we can
#start by combining the left number and the right number,
# if the sum is greater than target number, move largest number one place to the left
# if the sum is less than target number, move low number over to the right
# and the end, + 1 to our return low/high as position is different in programming language.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total > target:
                high -= 1
            elif total == target:
                return [low+1,high+1]
            else: 
                low += 1


#Runtime: 60 ms, faster than 83.80% of Python3 online submissions for Two Sum II - Input array is sorted.
#Memory Usage: 14.6 MB, less than 63.19% of Python3 online submissions for Two Sum II - Input array is sorted.
#08/08/2021 18:34	Accepted	60 ms	14.6 MB	python3
