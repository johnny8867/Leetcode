#Date:
#Question:
#Type: Easy


#Thoughts:
#Honestly I thought about enumerate and even hash table but I didn't continue with my thought
# this question is actually a bit more complicated than it looks
#it's using enumerate and Dictionary at the same time
#so for enumerate(num) it'll be
#0,1
#1,2
#2,3
#3,1
#and when we're making dictionary it'll be
#1,0
#2,1
#3,2
#and we're looping through i,v to see if v is in dic (the index)
#and if it is, i will compare with dic[v] (which is previous i)
#and return true if it is, else dic[v] will be replaced with new i

#honestly I'm 99% sure I wont remember how to do this question exactly LOL


nums = [1,2,3,1]
k = 3

dic = {}
for i, v in enumerate(nums):
    if v in dic and abs(i - dic[v]) <= k:
        print('true')
    dic[v] = i
    print(dic)
print('false')

#Runtime: 572 ms, faster than 98.06% of Python3 online submissions for Contains Duplicate II.
#Memory Usage: 28.2 MB, less than 65.45% of Python3 online submissions for Contains Duplicate II.
#08/16/2021 22:44	Accepted	572 ms	28.2 MB	python3
