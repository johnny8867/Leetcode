#Aug 07, 2021
#Question:
#一個人上台階可以一次上1個或者2個，問這個人上n階的台階，總共有幾種走法？
#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps.
#In how many distinct ways can you climb to the top?

#Thoughts:
#let n be amount of stairs, o be output
#if we draw out a table, we can see that
# n = 1, o = 1
# n = 2, o = 2
# n = 3, o = 3
# n = 4, o = 5
# n = 5, o = 8
#from the pattern we can see that output is determined by previous 2 output,
#so we can write a function that gives f(n-1)+f(n-2)
#and this will be done via recurrsion since our constant value is at n = 1 and n = 2

#eventually it's taking out the first step and making final step of either 1 or 2.


def stair(n):
    if n == 1:
        return 1;
    if n == 2:
        return 2;
    if n >2:
        return stair(n-1)+stair(n-2);

n=5
print(stair(n))
