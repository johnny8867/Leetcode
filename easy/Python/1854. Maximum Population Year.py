#Date Aug 7, 2021
#Type: Easy
#Question:
#You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

#The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

#Return the earliest year with the maximum population.


#Thoughts: I didn't understand the question at first, but once I understand it it makes sense

#The easiest way is to compute a list, and add in the number saw in the log file

# and at the end, produce the index value with max stored value, which is the population.

#Input: logs = [[1993,1999],[2000,2010]]
#Output: 1993
#Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

def maximumPopulation(self, logs: List[List[int]]) -> int:
    x=[0]*2050
    for start, end in logs:
        for i in range(start,end):
            x[i]+=1
    return(x.index(max(x)))
#Runtime: 88 ms, faster than 49.33% of Python3 online submissions for Concatenation of Array.
#Memory Usage: 14.6 MB, less than 55.21% of Python3 online submissions for Concatenation of Array.

#08/07/2021 14:54	Accepted	88 ms	14.6 MB	python3

