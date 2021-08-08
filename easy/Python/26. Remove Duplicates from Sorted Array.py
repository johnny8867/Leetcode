#Date:
#Question:

#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

#Type: Easy


#Thoughts:
    #Take out dups and count the list size.

nums = [1,1,2]

#new_nums = set(nums)


#print(new_nums)

#^ this isn't going to work becasue the question said  You must do this by modifying the input array in-place
#meaning u can't create a new list.



def removeDuplicates(List):
    nums[:] = sorted(set(nums))
    #print(nums)
    return len(nums)
print(removeDuplicates(nums))

#Runtime: 80 ms, faster than 88.82% of Python3 online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 15.6 MB, less than 84.53% of Python3 online submissions for Remove Duplicates from Sorted Array.
#08/08/2021 13:51	Accepted	80 ms	15.6 MB	python3
