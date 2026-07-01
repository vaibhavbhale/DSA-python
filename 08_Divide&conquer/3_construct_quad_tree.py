from typing import List
from collections import deque

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)
        
        # Check if grid is uniform
        same = True
        first = grid[0][0]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] != first:
                    same = False
                    break
        
        # If uniform → Leaf node
        if same:
            return Node(first == 1, True, None, None, None, None)
        
        # Divide into 4 parts
        half = n // 2
        
        topLeft = [row[:half] for row in grid[:half]]
        topRight = [row[half:] for row in grid[:half]]
        bottomLeft = [row[:half] for row in grid[half:]]
        bottomRight = [row[half:] for row in grid[half:]]
        
        return Node(
            True,
            False,
            self.construct(topLeft),
            self.construct(topRight),
            self.construct(bottomLeft),
            self.construct(bottomRight)
        )


# ---------------- INPUT ----------------
grid = [
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0]
]

obj = Solution()
root = obj.construct(grid)


# -------- LEVEL ORDER PRINT --------
def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            result.append([int(node.isLeaf), int(node.val)])
            
            if not node.isLeaf:
                queue.append(node.topLeft)
                queue.append(node.topRight)
                queue.append(node.bottomLeft)
                queue.append(node.bottomRight)
        else:
            result.append(None)
    
    return result


print("Output:")
print(levelOrder(root))

"""======================== DRY RUN ========================

STEP 1:
Call construct() on 8x8 grid.

Check if uniform:
- first value = 1
- grid contains 0 also → NOT uniform

So divide into 4 parts (each 4x4).

---------------------------------------------------------

STEP 2: TopLeft (4x4)

1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

All 1 → uniform
Return Leaf(True)

---------------------------------------------------------

STEP 3: TopRight (4x4)

0 0 0 0
0 0 0 0
1 1 1 1
1 1 1 1

Mixed values → divide into 4 (2x2 each)

TopLeft:
0 0
0 0
→ Leaf(False)

TopRight:
0 0
0 0
→ Leaf(False)

BottomLeft:
1 1
1 1
→ Leaf(True)

BottomRight:
1 1
1 1
→ Leaf(True)

---------------------------------------------------------

STEP 4: BottomLeft (4x4)

1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

All 1 → Leaf(True)

---------------------------------------------------------

STEP 5: BottomRight (4x4)

0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

All 0 → Leaf(False)

---------------------------------------------------------

FINAL TREE STRUCTURE:

Root (isLeaf=False)
   ├── TopLeft     → Leaf(True)
   ├── TopRight    → Internal Node
   │       ├── Leaf(False)
   │       ├── Leaf(False)
   │       ├── Leaf(True)
   │       └── Leaf(True)
   ├── BottomLeft  → Leaf(True)
   └── BottomRight → Leaf(False)

---------------------------------------------------------

Stopping Condition:
Recursion stops whenever region becomes uniform.

Time Complexity: O(n^2 log n)
Space Complexity: O(log n)

=========================================================
"""