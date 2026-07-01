# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev_val = None

        def dfs(root):
            if not root:
                return

            # Traverse left subtree
            dfs(root.left)

            # Compare current node with previous node
            if self.prev_val is not None:
                self.min_diff = min(
                    self.min_diff,
                    abs(root.val - self.prev_val)
                )

            # Update previous node value
            self.prev_val = root.val

            # Traverse right subtree
            dfs(root.right)

        dfs(root)
        return self.min_diff


# Input: root = [4,2,6,1,3]

# Creating the tree manually:
#         4
#       /   \
#      2     6
#     / \
#    1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
print(sol.getMinimumDifference(root))


"""
Dry Run for root = [4,2,6,1,3]

Tree:
        4
       / \
      2   6
     / \
    1   3


Initial:
self.min_diff = inf
self.prev_val = None


Call dfs(4)

Step 1:
Go Left -> dfs(2)

    Step 2:
    Go Left -> dfs(1)

        Step 3:
        Go Left -> dfs(None)
        return

        Process Node 1:
        prev_val = None
        No comparison

        Update:
        prev_val = 1

        Go Right -> dfs(None)
        return


    Process Node 2:
    diff = abs(2 - 1)
    diff = 1

    min_diff = min(inf,1)
    min_diff = 1

    Update:
    prev_val = 2

    Go Right -> dfs(3)

        Step 4:
        Go Left -> dfs(None)
        return

        Process Node 3:
        diff = abs(3 - 2)
        diff = 1

        min_diff = min(1,1)
        min_diff = 1

        Update:
        prev_val = 3

        Go Right -> dfs(None)
        return


Process Node 4:
diff = abs(4 - 3)
diff = 1

min_diff = min(1,1)
min_diff = 1

Update:
prev_val = 4

Go Right -> dfs(6)

    Step 5:
    Go Left -> dfs(None)
    return

    Process Node 6:
    diff = abs(6 - 4)
    diff = 2

    min_diff = min(1,2)
    min_diff = 1

    Update:
    prev_val = 6

    Go Right -> dfs(None)
    return


Inorder Traversal:
1 -> 2 -> 3 -> 4 -> 6

Differences:
2-1 = 1
3-2 = 1
4-3 = 1
6-4 = 2

Minimum Difference:
1

Final Output:
1
"""