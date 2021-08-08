#Date: Aug 7,2021
#Note, I was never good at Dictinaries LOL
#Question:In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

#Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#Type: Easy


#Thoughts:
#First we should make a dictionary that produces the number order corresponding to alphabet
#Then break our words into characters and use our dictionary to compare with the other word
#Make sure to have if cases if same character but different length.
#^make sure to take account cases like app, apple and apple, app


words = ["app","apple"]
order = "abcdefghijklmnopqrstuvwxyz"



def isAlienSorted(words, order):
    dic = {}

    for i in range(len(order)):
        dic[order[i]] = i

    first = words[0]

    for word in words:

        if word == first:
            continue
        if (len(word) < len(first)) and word == first[:len(word)]:
            return False
        print(first)
        print(word)
        print('**')
        print(word[:len(first)])
        if (len(word) > len(first)) and (first == word[:len(first)]):
            print('here')
            return True
        for i in range(0, len(word)):
            if dic[word[i]] > dic[first[i]]:
                break
            if dic[word[i]] < dic[first[i]]:
                return False
            first = word
    return True


print(isAlienSorted(words,order))

#Runtime: 32 ms, faster than 85.78% of Python3 online submissions for Verifying an Alien Dictionary.
#Memory Usage: 14.4 MB, less than 17.38% of Python3 online submissions for Verifying an Alien Dictionary.
#08/07/2021 18:33	Accepted	32 ms	14.4 MB	python3
