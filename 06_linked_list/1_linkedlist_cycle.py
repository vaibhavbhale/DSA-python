from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
       
        while fast and fast.next:
            slow = slow.next         
            fast = fast.next.next    
                        
            if slow == fast:
                return True
        
        return False

arr = [3,2,0,-4]
pos = 1

# -------------------------
# Convert list to LinkedList
# -------------------------
nodes = [ListNode(val) for val in arr]

for i in range(len(arr) - 1):
    nodes[i].next = nodes[i + 1]

# Create cycle
if pos != -1:
    nodes[-1].next = nodes[pos]

head = nodes[0]

print(Solution().hasCycle(head))   
    
    # Example 1: List with cycle
        #
        # 1 → 2 → 3 → 4 → 5
        #           ↑     ↓
        #           ← ← ← ←
        #
        # Step-by-step dry run:
        #
        # Step 0:
        # slow = 1
        # fast = 1
        #
        # Step 1:
        # slow moves 1 step → 2
        # fast moves 2 steps → 3
        #
        # Step 2:
        # slow → 3
        # fast → 5
        #
        # Step 3:
        # slow → 4
        # fast → 4
        #
        # slow == fast → cycle detected → return True
        
    
     # Example 2: List without cycle
        #
        # 1 → 2 → 3 → 4 → 5 → None
        #
        # Step 0:
        # slow = 1
        # fast = 1
        #
        # Step 1:
        # slow → 2
        # fast → 3
        #
        # Step 2:
        # slow → 3
        # fast → 5
        #
        # Step 3:
        # slow → 4
        # fast → None
        #
        # fast becomes None → loop stops → return False
        