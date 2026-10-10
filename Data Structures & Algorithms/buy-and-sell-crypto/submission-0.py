class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers
        #one for buy and one for sell
        left = 0
        right = 1
        maxProfit = 0

        while (right < len(prices)) :
            #check if profitable
            if prices[left] < prices[right] :
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else :
                #not profitable, meaning we need to move left and right
                #since if statement failed that means the right is at our lowest right now, so we want left to be that
                left = right
            #on every iteration increment right
            right += 1
        
        return maxProfit
