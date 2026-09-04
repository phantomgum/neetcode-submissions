class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstMap = {}
        secondMap = {}
        for letter in s :
            #we've seen this letter before
            if letter in firstMap :
                firstMap[letter] += 1
            else :
                #we haven't seen this letter before
                firstMap[letter] = 1
        for letter in t :
            #we've seen this letter before
            if letter in secondMap :
                secondMap[letter] += 1
            else :
                #we haven't seen this letter before
                secondMap[letter] = 1
        if firstMap == secondMap :
            return True
        return False


