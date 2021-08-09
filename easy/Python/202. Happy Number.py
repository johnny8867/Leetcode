#Date:080821

# I think this is one of the question that I iwon't really remember how to solve the next time I see it LOL

#Question:

#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.

#Type: Easy


#Thoughts:
#Honestly I think this is slightly complicated question, really need to understand the question
#https://leetcode.com/problems/happy-number/discuss/560849/My-simple-Python-recursive-solution
#so write down a table and see how each number will go to
# 1^2 =1 , 2^2 =4 , 3^2 = 9, 4^2=16 ... 4 , 5^2 = 25 ...89
#64+81 = 1 4 5 = > 42 and loops back to 4
# 6^2 = 36 so it's 9,
#7^2 = 49 ... 1
#8^2 = 64 => 52 => 29 ...
#9^2 = 81 ...89
#so we can see that only 1 and 7 will eventually produce 1
#Then we can write a recursive that will keep checking if the number ever goes
# to 1 or 7, if not, return False.

class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        for item in str(n):
            digit = int(item)
            total += digit*digit
            
        if total ==1 or total ==7:
            return True
        
        else:
            if total < 10 or total ==0:
                return False
            else:
                return self.isHappy(total)

#Runtime: 28 ms, faster than 95.08% of Python3 online submissions for Happy Number.
#Memory Usage: 14.3 MB, less than 49.76% of Python3 online submissions for Happy Number.
#08/08/2021 18:08	Accepted	28 ms	14.3 MB	python3
        
        
