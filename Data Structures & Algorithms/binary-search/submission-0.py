class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if not nums :
            return -1

        while (left <= right) :
            #calculate mid point
            mid = (left + right) // 2

            #check where target is
            if target > nums[mid] :
                left = mid + 1
            elif target < nums[mid] :
                right = mid - 1
            else :
                #the mid is our target
                return mid
            
        return -1
        