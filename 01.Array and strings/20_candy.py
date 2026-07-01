class Solution:
    def candy(self, ratings): 
        n = len(ratings)
        candies = [1] * n
    
        # LEFT → RIGHT PASS
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        
        # RIGHT → LEFT PASS
        for i in range(n - 2, -1, -1): 
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        
        return sum(candies)  # 2 + 1 + 2 = 5

print(Solution().candy([1,0,2]))
        
           # LEFT → RIGHT PASS
            # i = 1
            # ratings[1] = 0
            # ratings[0] = 1
            # 0 > 1 ❌ No change
            # candies = [1,1,1]
            
            # i = 2
            # ratings[2] = 2
            # ratings[1] = 0
            # 2 > 0 ✅
            # candies[2] = candies[1] + 1 = 2
            # candies = [1,1,2]
            
            
        #RIGHT → LEFT PASS
        #for i in range(n - 2, -1, -1):
            
            # i = 1
            # ratings[1] = 0
            # ratings[2] = 2
            # 0 > 2 ❌ No change
            # candies = [1,1,2]
            
            # i = 0
            # ratings[0] = 1
            # ratings[1] = 0
            # 1 > 0 ✅
            # candies[0] = max(1, candies[1] + 1)
            # candies[0] = max(1, 2) = 2
            # candies = [2,1,2]
    