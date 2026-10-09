class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #calculate the master product of everything in the array
        master = 1
        #count how many zeroes appear
        count = 0

        output = [0] * len(nums)
        for i in nums :
            #we don't want to multiply by 0, since it will ruin the master product
            if i != 0 :
                master *= i
            else :
                count += 1
            
        #if 2 or more zeroes that means every product will always be zero
        if count >= 2 :
            return output
        
        if count == 1 :
            for j in range(len(output)) :
                if nums[j] == 0 :
                    output[j] = master
            
            return output
        
        #calculate the products for each index in output
        for j in range(len(output)) :
            if nums[j] == 0 :
                output[j] = master
            else :
                output[j] = master // nums[j]
        
        return output