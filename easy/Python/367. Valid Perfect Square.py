#Date Aug 7, 2021
#Type: Easy
#Question:
#Given a positive integer num, write a function which returns True if num is a perfect square else False.



#Thoughts: since num**0.5 will return as float, we will have to check it with int(num**05)

# if produce a whole number, then return true, else false :)
num = 15

def isPerfectSquare(self, num: int) -> bool:
    if (num**0.5 == int(num**0.5)):
        return True
    else:
        return False

#Runtime: Runtime: 32 ms, faster than 60.11% of Python3 online submissions for Valid Perfect Square.
#Memory Usage: 14.3 MB, less than 6.41% of Python3 online submissions for Valid Perfect Square.
#08/08/2021 01:07	Accepted	32 ms	14.3 MB	python3
