# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root, ans):
        if root is None:
            return

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

    def kthSmallest(self, root, k):
        ans = []
        self.inorder(root, ans)
        return ans[k - 1]

# root = [3,1,4,null,2]

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

k = 1

obj = Solution()
print(obj.kthSmallest(root, k))


# ==========================================================
# Dry Run
# ==========================================================
#
# Input:
# root = [3,1,4,null,2]
# k = 1
#
# Binary Tree:
#
#         3
#        / \
#       1   4
#        \
#         2
#
# Step 1:
# ans = []
#
# Call:
# obj.kthSmallest(root, 1)
#
# Step 2:
# inorder(3)
#
# -> Move to left child (1)
#
#    inorder(1)
#
#    -> Move to left child (None)
#       Return
#
#    -> Visit node 1
#       ans = [1]
#
#    -> Move to right child (2)
#
#       inorder(2)
#
#       -> Left = None
#          Return
#
#       -> Visit node 2
#          ans = [1, 2]
#
#       -> Right = None
#          Return
#
# Return to node 3
#
# Step 3:
# Visit node 3
# ans = [1, 2, 3]
#
# Step 4:
# Move to right child (4)
#
#    inorder(4)
#
#    -> Left = None
#       Return
#
#    -> Visit node 4
#       ans = [1, 2, 3, 4]
#
#    -> Right = None
#       Return
#
# Traversal Finished
#
# Final ans = [1, 2, 3, 4]
#
# Return:
# ans[k-1]
# = ans[0]
# = 1
#
# Output:
# 1
# ==========================================================