#Date:
#Question:
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#Type: Easy


#Thoughts:
#have a store to store if number is negative
#use [::-1] to reverse
#make sure convert to str, do the operation and switch back to int
#use bit_length to check if the length is greater than 32 or not

def reverse(x):
    if str(x)[0] =='-':
        store = True
        x = abs(x)
            
    else:
        store = False
        
    x = str(x)
    x = x[::-1]
    print(int(x).bit_length())
    if store == True:
        return int(x)*(-1) if int(x).bit_length() < 32 else 0
    else:
        return int(x) if int(x).bit_length() < 32 else 0

print(reverse(1534236469))

#Runtime: 28 ms, faster than 88.39% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.2 MB, less than 45.11% of Python3 online submissions for Reverse Integer.
#08/08/2021 18:53	Accepted	28 ms	14.2 MB	python3
