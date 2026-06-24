from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        

        curr = prev.next
        
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
         
        return dummy.next

values = [1, 2, 3, 4, 5]
left = 2
right = 4

# Convert list to linked list
head = ListNode(values[0])
current = head

for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

# Call function
solution = Solution()
new_head = solution.reverseBetween(head, left, right)

# Print result
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
    
# ==========================
# DRY RUN
# ==========================

# Input:
# head = 1 → 2 → 3 → 4 → 5
# left = 2
# right = 4

# Step 1:
# Create dummy node
# dummy → 0 → 1 → 2 → 3 → 4 → 5
# prev = dummy

# Step 2:
# Move prev (left - 1 = 1 time)
# prev → 1
# List:
# 0 → 1 → 2 → 3 → 4 → 5

# Step 3:
# curr = prev.next
# curr → 2

# We reverse (right - left = 2 times)

# -------------------------
# Iteration 1
# -------------------------
# temp = curr.next → 3
# curr.next = temp.next → 2 → 4
# temp.next = prev.next → 3 → 2
# prev.next = temp → 1 → 3

# List becomes:
# 1 → 3 → 2 → 4 → 5


# -------------------------
# Iteration 2
# -------------------------
# temp = curr.next → 4
# curr.next = temp.next → 2 → 5
# temp.next = prev.next → 4 → 3
# prev.next = temp → 1 → 4

# List becomes:
# 1 → 4 → 3 → 2 → 5


# Final Output:
# 1 → 4 → 3 → 2 → 5