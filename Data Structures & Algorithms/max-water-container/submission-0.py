class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two points to start at left and right bars
        left = 0
        right = len(heights) - 1
        maximum = (right - left) * min(heights[left], heights[right])

        while left < right :
            #check which bar has is shorter
            if heights[left] < heights[right] :
                left += 1
            else :
                #increment the right
                right -= 1
            
            #now we'll calculate the new max amount of water
            container = (right - left) * min(heights[left], heights[right])
            #update our max
            maximum = max(maximum, container)
        
        return maximum