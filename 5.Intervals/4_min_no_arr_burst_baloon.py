from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        cnt = 1   
        end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > end:
                cnt += 1
                end = points[i][1]

        return cnt


print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

# -----------------------------
            # i = 1 → balloon = [2,8]
            # Check: 2 > 6 ? → False
            # Overlaps with arrow at 6
            # No new arrow needed
            # cnt = 1
            # end = 6
            # -----------------------------
            
            # i = 2 → balloon = [7,12]
            # Check: 7 > 6 ? → True
            # No overlap
            # Need new arrow
            # cnt = 2
            # end = 12 (Arrow 2 shot at 12)
            # -----------------------------
            
            # i = 3 → balloon = [10,16]
            # Check: 10 > 12 ? → False
            # Overlaps with arrow at 12
            # No new arrow needed
            # cnt = 2
            # end = 12
            # -----------------------------
            