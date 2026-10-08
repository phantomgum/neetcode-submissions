class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two hashmaps to stores letter frequency for each string
        sMap = {}
        tMap = {}

        #loop through both strings and store the frequencies in the hash maps
        for char in s :
            if char in sMap :
                sMap[char] += 1
            else :
                sMap[char] = 1

        for char in t :
            if char in tMap :
                tMap[char] += 1
            else :
                tMap[char] = 1

        #hashmaps are filled with the letter frequencies
        #are they equal
        if sMap == tMap :
            return True
        
        return False