class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        if len(prices) < 2:
            return 0
        
        n = len(prices) - 1

        left = 0
        right = 1
        res = 0

        while right < n:
            if prices[right] - prices[left] < 0:
                left += 1
                
            else:
                res = max(res, prices[right] - prices[left])
            right += 1  
        
        while left < right:
            if prices[right] - prices[left] > 0:
                 res = max(res, prices[right] - prices[left])
            left += 1
               

        return res


        