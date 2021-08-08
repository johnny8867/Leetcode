#Date:
#Question:
#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Type: Easy


#Thoughts:
# I like the recurrsion method better 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            a = 0
            b = 1
            c = a
            for i in range(n):
                c = a
                a = b
                b = c + b
            return b
#            return climbStairs(n-1)+climbStairs(n-2)
