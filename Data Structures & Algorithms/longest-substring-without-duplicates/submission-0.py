class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        #use a hashset to keep track of
        #duplicates
        duplicates = set()
        #left side of window
        l = 0
        
        for r in range(len(s)) :
            while s[r] in duplicates :
                #increment our left and remove that char from the set
                duplicates.remove(s[l])
                l += 1
            duplicates.add(s[r])
            longest = max(longest, r - l + 1)

        return longest

