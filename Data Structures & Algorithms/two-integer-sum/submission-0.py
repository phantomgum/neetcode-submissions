class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #need a hashmap to store the number and its index
        map = {}

        for index, num in enumerate(nums) :
            complement = target - num
            #check if the complement is in the map
            if complement in map :
                return [map[complement], index]
            #if not in there, then add the num to the map
            map[num] = index
        