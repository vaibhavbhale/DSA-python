class solution:
    def maxprofit(self,prices:list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for p in prices:
            max_profit = max(max_profit,p - min_price) # max=0,p=7-7=0.....
            min_price = min(min_price,p) # 0 ,7 min =0
         
        return max_profit
    
prices=[7,1,5,3,6,4]
print(solution().maxprofit(prices))

  # ---- Iteration 1 ----
            # p = 7
            # profit = 7 - 7 = 0
            # max_profit = max(0, 0) = 0
            # min_price = min(7, 7) = 7
            
            # ---- Iteration 2 ----
            # p = 1
            # profit = 1 - 7 = -6
            # max_profit = max(0, -6) = 0
            # min_price = min(7, 1) = 1
            
            # ---- Iteration 3 ----
            # p = 5
            # profit = 5 - 1 = 4
            # max_profit = max(0, 4) = 4
            # min_price = min(1, 5) = 1
            
            # ---- Iteration 4 ----
            # p = 3
            # profit = 3 - 1 = 2
            # max_profit = max(4, 2) = 4
            # min_price = min(1, 3) = 1
            
            # ---- Iteration 5 ----
            # p = 6
            # profit = 6 - 1 = 5
            # max_profit = max(4, 5) = 5
            # min_price = min(1, 6) = 1
            
            # ---- Iteration 6 ----
            # p = 4
            # profit = 4 - 1 = 3
            # max_profit = max(5, 3) = 5
            # min_price = min(1, 4) = 1