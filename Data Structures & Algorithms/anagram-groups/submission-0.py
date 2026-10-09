class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #don't use a sort
        #we'll use a hashmap
        map = defaultdict(list)

        for word in strs :
            #iterate through each char
            #have array to track letter frequencies from a-z
            frequency = [0] * 26
            for char in word :
                #now we need to map a -> 0 and b -> 1, and so on
                frequency[ord(char) - ord("a")] += 1
            #now add that word to the hashmap using its letter frequency array as the key
            map[tuple(frequency)].append(word)
        
        return list(map.values())
