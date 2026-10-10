class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r :
            mid = (l + r) // 2
            if nums[mid] == target :
                return mid

            #check which side of the array we are in
            #left sorted portion or right sorted portion?
            if nums[mid] >= nums[l] :
                #we are in left side
                #lets check if our target is here though
                #if target is > middle or < the left, its in the right side
                if target > nums[mid] or target < nums[l]:
                    #search right side
                    l = mid + 1
                else :
                    #target is in left side
                    r = mid - 1

            else : #we are in right side
                
                if target < nums[mid] or target > nums[r]:
                    #go to the left
                    r = mid - 1
                else :#target is > mid and < right value
                    #search right portion
                    l = mid + 1
        return -1

