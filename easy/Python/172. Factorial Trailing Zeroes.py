#Date:081521
#Question:
#Given an integer n, return the number of trailing zeroes in n!.

#Follow up: Could you write a solution that works in logarithmic time complexity?

#Type: Easy


#Thoughts:
#honestly... understand the formula and you'll be good for the answer
#so basically to find out the trailing zeroes, it's determined on how many *10
#it is in the factorial, and it's break into 2 * 5
#so we find out how many time a number can be divided by 2 and 5
#clearly, number of time divided by 5 is much less than 2, so we will
#implement a solution based on 5
#e.g, 60
# 60 // 5 = 12
#however, there is numbers like 25 and 50 which is 5*5 and 2*5*5 (meaning
# it has number that can be divided by 5 again)
#you can use recusive method to solve it, but I did a while loop
# using a while loop because there might be numbers that's like 5*5*5*5,
#so using while loop will keep looping until the condition is met.
#then we just add the numbers that's // by 5 and add the while loop ones.

def trailingZeroes(n):
    number = n //5
    total = number
    while number >= 5:
        total += (number//5)
        number = number //5
    return total

print(trailingZeroes(80))


#Runtime: 24 ms, faster than 97.08% of Python3 online submissions for Factorial Trailing Zeroes.
#Memory Usage: 14.2 MB, less than 49.87% of Python3 online submissions for Factorial Trailing Zeroes.
#08/15/2021 15:37	Accepted	24 ms	14.2 MB	python3
