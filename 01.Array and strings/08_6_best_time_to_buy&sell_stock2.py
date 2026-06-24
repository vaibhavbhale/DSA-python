from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1] : # 1 > 7 false 
                profit += prices[i] - prices[i-1]  # 1 - 7 = -6 < 0  profit 0
                
        return  profit        
            
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))