#Date:
#Question:
#Type: Easy


#Thoughts:
    #The only thing that we have to worry about is # 4,9,40,90,400,900 as 1,2,3,5,6,7,8 we can produce it with symbol
    #so we just write replace statements, and then search through Dictionary.



def romanToInt(self, s: str) -> int:
        
    Dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
    total = 0
    s = s.replace("IV","IIII").replace("IX","VIIII")
    s = s.replace("XL", "XXXX").replace("XC","LXXXX")
    s = s.replace("CD","CCCC").replace("CM","DCCCC")
        
    for item in s:
        total += Dic[item]
            
    return total

#Runtime: 44 ms, faster than 81.47% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14.2 MB, less than 83.81% of Python3 online submissions for Roman to Integer.
#08/08/2021 13:16	Accepted	44 ms	14.2 MB	python3
