#Date:081221

#Question:
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


#Type: Easy


#Thoughts:
#so I saw that the len of nums1 is m+n, and since this question asked use to just modify nums1,
#we can use [:] to shallow-copies the list of nums1, and use the sort function and add up the list of nums1 and nums2 to it's appropriate length of m and n

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(sorted(nums1[:m]+nums2[:n]))
        nums1[:] = sorted(nums1[:m]+nums2[:n])
        


        
#        while n>0 and m>0:
#            if nums1[m-1] > nums2[n-1]:
#                nums1[m + n - 1] = nums1[m-1]
#                m -= 1
#            else:
#                nums1[m + n - 1] = nums2[n-1]
#                n -= 1
#        while n > 0:
#            nums1[n-1] = nums2[n-1]
#            n -= 1
                



#Runtime: 32 ms, faster than 89.46% of Python3 online submissions for Merge Sorted Array.
#Memory Usage: 14.3 MB, less than 63.25% of Python3 online submissions for Merge Sorted Array.
#08/11/2021 23:47	Accepted	32 ms	14.3 MB	python3
