from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0 
                start = i+1 
        return start

    
print(Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))

 
        # gas  = [1,2,3,4,5]
        # cost = [3,4,5,1,2]
        
        # Step 1: Check total gas vs total cost
        # sum(gas)  = 15
        # sum(cost) = 15
        # Since sum(cost) <= sum(gas), solution exists
        
         # i = 0
        # tank = 0 + (1 - 3) = -2
        # tank < 0 → reset tank and move start
        # tank = 0
        # start = 1
        
        # i = 1
        # tank = 0 + (2 - 4) = -2
        # tank < 0 → reset tank and move start
        # tank = 0
        # start = 2
        
        # i = 2
        # tank = 0 + (3 - 5) = -2
        # tank < 0 → reset tank and move start
        # tank = 0
        # start = 3
        
        # i = 3
        # tank = 0 + (4 - 1) = 3
        # tank >= 0 → continue
        
        # i = 4
        # tank = 3 + (5 - 2) = 6
        # tank >= 0 → continue
        