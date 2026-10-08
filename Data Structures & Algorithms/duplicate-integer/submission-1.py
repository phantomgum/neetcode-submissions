class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use a hash set to track duplicates
        seen = set()

        for num in nums :
            if num in seen :
                #we have a duplicate
                return True
            else :
                #we haven't seen the number before
                seen.add(num)
        return False
        