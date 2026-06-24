from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = group_prev
            
            # Find kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            
            # Reverse group
            prev = group_next
            curr = group_prev.next
            
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp


# ---------------- INPUT ----------------
arr = [1, 2, 3, 4, 5]
k = 2

# Convert list to linked list
def createLinkedList(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

head = createLinkedList(arr)

# ---------------- FUNCTION CALL ----------------
obj = Solution()
result = obj.reverseKGroup(head, k)

# ---------------- PRINT RESULT ----------------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("Reversed in K-Group:")
printList(result)


"""
========================= DRY RUN =========================

Input:
1 -> 2 -> 3 -> 4 -> 5
k = 2

-----------------------------------------------------------
STEP 1: First Group (1,2)

group_prev = dummy
Find kth node:
kth moves 2 steps → node = 2

group_next = 3

Now reverse between 1 and 2:

Initial:
prev = 3
curr = 1

Iteration 1:
temp = 2
1.next = 3
prev = 1
curr = 2

Iteration 2:
temp = 3
2.next = 1
prev = 2
curr = 3 (stop because curr == group_next)

Now group becomes:
2 -> 1 -> 3 -> 4 -> 5

Move group_prev to 1

-----------------------------------------------------------
STEP 2: Second Group (3,4)

group_prev = 1
Find kth:
kth moves 2 steps → node = 4

group_next = 5

Reverse (3,4):

prev = 5
curr = 3

Iteration 1:
3.next = 5
prev = 3
curr = 4

Iteration 2:
4.next = 3
prev = 4
curr = 5 (stop)

Now list:
2 -> 1 -> 4 -> 3 -> 5

Move group_prev to 3

-----------------------------------------------------------
STEP 3: Remaining Node (5)

Try to find kth:
Only 1 node left (< k)
So stop.

-----------------------------------------------------------

FINAL OUTPUT:
2 -> 1 -> 4 -> 3 -> 5

Time Complexity: O(n)
Space Complexity: O(1)

===========================================================
"""