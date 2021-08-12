#Date:081221

#Question:
#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Type: Easy


#Thoughts:
#write a for loop, check if number is alphanum(), not justl.isalpha(),
#then put into a string if it's true,
#then use .lower() to make the format consist
#then use [::-1] (reverse) to compare to our new string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for character in s:
            if character.isalnum():
                string +=character

        print(string)
        if (string[::-1].lower() == string.lower()):
            return True
        else:
            return False



#Runtime: 40 ms, faster than 87.35% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 14.8 MB, less than 50.15% of Python3 online submissions for Valid Palindrome.
#08/12/2021 00:58	Accepted	40 ms	14.8 MB	python
