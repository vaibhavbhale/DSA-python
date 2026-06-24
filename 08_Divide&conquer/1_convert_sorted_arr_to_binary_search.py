from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recur(nums):
            n = len(nums)
            
            # Base case
            if n == 0:
                return None
            
            # Find middle index
            mid = n // 2
            
            # Create root node
            node = TreeNode(nums[mid])
            
            # Recursively build left and right subtree
            node.left = recur(nums[0:mid])
            node.right = recur(nums[mid+1:n])
            
            return node
        
        return recur(nums)


# ----------- TAKING INPUT -------------
nums = [1, 3]

# ----------- FUNCTION CALL -------------
obj = Solution()
root = obj.sortedArrayToBST(nums)


# ----------- INORDER TRAVERSAL TO VERIFY -------------
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

print("Inorder Traversal of BST:")
inorder(root)


"""
================= DRY RUN =================

Input:
nums = [1, 3]

STEP 1:
Call sortedArrayToBST([1,3])
→ Calls recur([1,3])

---------------------------------

STEP 2:
recur([1,3])
n = 2
mid = 2 // 2 = 1

nums[mid] = nums[1] = 3

Create node = TreeNode(3)

Now build:
Left subtree  = recur([1])
Right subtree = recur([])

---------------------------------

STEP 3:
recur([1])
n = 1
mid = 1 // 2 = 0

nums[mid] = nums[0] = 1

Create node = TreeNode(1)

Left subtree  = recur([])
Right subtree = recur([])

---------------------------------

STEP 4:
recur([]) → return None

So node 1 becomes:
      1
     / \
  None None

---------------------------------

STEP 5:
Right subtree of 3:
recur([]) → return None

---------------------------------

FINAL TREE:

        3
       /
      1

---------------------------------

Inorder Traversal Output:
1 3

Tree is Balanced BST ✔

=================================
"""