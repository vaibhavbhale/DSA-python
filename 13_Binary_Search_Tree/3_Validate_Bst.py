# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, root, mn, mx):
        if root is None:
            return True

        if root.val < mn or root.val > mx:
            return False

        checkleft = self.check(root.left, mn, root.val - 1)
        checkright = self.check(root.right, root.val + 1, mx)

        return checkleft and checkright

    def isValidBST(self, root):
        return self.check(root, -10000000000000000, 10000000000000000)

root = [2,1,3]

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

obj = Solution()
print(obj.isValidBST(root))


# ==========================================================
# Dry Run
# ==========================================================
#
# Input:
# root = [2,1,3]
#
# Binary Tree:
#
#        2
#       / \
#      1   3
#
# Initial Call:
#
# isValidBST(root)
# -> check(2, -∞, +∞)
#
# ----------------------------------------------------------
# Step 1:
# Current Node = 2
#
# Allowed Range:
# [-∞, +∞]
#
# Is 2 within the range?
# Yes
#
# Check Left Subtree:
# check(1, -∞, 1)
#
# Check Right Subtree:
# check(3, 3, +∞)
#
# ----------------------------------------------------------
# Step 2 (Left Subtree):
#
# Current Node = 1
#
# Allowed Range:
# [-∞, 1]
#
# Is 1 within the range?
# Yes
#
# Left Child:
# check(None, -∞, 0)
# Returns True
#
# Right Child:
# check(None, 2, 1)
# Returns True
#
# Left Subtree Result:
# True
#
# ----------------------------------------------------------
# Step 3 (Right Subtree):
#
# Current Node = 3
#
# Allowed Range:
# [3, +∞]
#
# Is 3 within the range?
# Yes
#
# Left Child:
# check(None, 3, 2)
# Returns True
#
# Right Child:
# check(None, 4, +∞)
# Returns True
#
# Right Subtree Result:
# True
#
# ----------------------------------------------------------
# Final Result:
#
# checkleft  = True
# checkright = True
#
# Return:
# True AND True
# = True
#
# Output:
# True
# ==========================================================