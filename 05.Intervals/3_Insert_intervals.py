from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals,newInterval))

'''

        # intervals = [[1,3],[6,9]]
        # newInterval = [2,5]
        
        result = []
        i = 0

        # -----------------------------
        # Step 1: Add intervals before newInterval
        # Condition: intervals[i][1] < newInterval[0]
        #
        # i = 0
        # intervals[0] = [1,3]
        # 3 < 2 ? → No
        #
        # So skip this loop (nothing added)
        # -----------------------------
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # -----------------------------
        # Step 2: Merge overlapping intervals
        #
        # i = 0
        # intervals[0] = [1,3]
        # 1 <= 5 ? → Yes (overlap)
        #
        # newInterval[0] = min(2,1) = 1
        # newInterval[1] = max(5,3) = 5
        # newInterval becomes [1,5]
        # i = 1
        #
        # i = 1
        # intervals[1] = [6,9]
        # 6 <= 5 ? → No (stop merging)
        # -----------------------------
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # After merging:
        # newInterval = [1,5]
        # result = []
        
        result.append(newInterval)
        # result = [[1,5]]

        # -----------------------------
        # Step 3: Add remaining intervals
        #
        # i = 1
        # intervals[1] = [6,9]
        # Add it
        # result = [[1,5],[6,9]]
        # -----------------------------
        
'''