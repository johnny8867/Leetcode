#Date: Aug 07, 2021
#Question:

#Given a non-negative integer x, compute and return the square root of x.

#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

#Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

#Type: Easy

#Thoughts:
#First deal with the case when x == 0 and 1,
#Also since the decimal is truncated, no decimal (meaning rounds down)
#Then write a loop that will check from 1 to x+1,
#if there is a number * itself will give the x value, return
#elif the number * itself is greater than x and a (number-1) * itself is less than x,
#return that number and round down.

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1,x+1):
            if i*i == x:
                return i
            elif i*i > x and (i-1)*(i-1) < x:
                return i-1


#Runtime: 2736 ms, faster than 8.28% of Python3 online submissions for Sqrt(x).
#Memory Usage: 14 MB, less than 97.88% of Python3 online submissions for Sqrt(x).
#08/07/2021 18:48	Accepted	2736 ms	14 MB	python3
