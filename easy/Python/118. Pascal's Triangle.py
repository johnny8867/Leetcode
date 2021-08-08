#Date:080821
#Question:
#Given an integer numRows, return the first numRows of Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


#Type: Easy

#Thoughts: Really impressive about line 2... I don't think I have ever seen it..
#this question is kind of similar of what I did in 3SK3 project 1,
#where interpolation took pixel from four side, while this one took the upper two
#Just gotta make sure not confused by the pattern...

    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range (numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal



#Runtime: 32 ms, faster than 58.35% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 14.1 MB, less than 82.76% of Python3 online submissions for Pascal's Triangle.
#08/08/2021 14:33	Accepted	32 ms	14.1 MB	python3
