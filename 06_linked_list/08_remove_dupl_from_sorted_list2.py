from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # If duplicate sequence found
            if head.next and head.val == head.next.val:
                
                # Skip all duplicates
                while head.next and head.val == head.next.val:
                    head = head.next
                
                # Remove duplicate block
                prev.next = head.next
            else:
                prev = prev.next
            
            head = head.next
        
        return dummy.next


# ---------------- INPUT ----------------
arr = [1, 2, 3, 3, 4, 4, 5]

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
result = obj.deleteDuplicates(head)

# ---------------- PRINT RESULT ----------------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("After Removing All Duplicates:")
printList(result)


"""
=========================== DRY RUN ===========================

Input:
1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5

Goal:
Remove ALL nodes that have duplicates.
Only unique numbers remain.

---------------------------------------------------------------
Initial:
dummy -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
prev = dummy
head = 1

---------------------------------------------------------------
Iteration 1:
head = 1
No duplicate (1 != 2)
prev = 1
head = 2

---------------------------------------------------------------
Iteration 2:
head = 2
No duplicate (2 != 3)
prev = 2
head = 3

---------------------------------------------------------------
Iteration 3:
head = 3
Duplicate found (3 == 3)

Move head until duplicates end:
head moves from first 3 → second 3

Now head at second 3
Remove duplicate block:
prev.next = head.next
2.next = 4

List becomes:
1 -> 2 -> 4 -> 4 -> 5

Move head to next:
head = 4

---------------------------------------------------------------
Iteration 4:
head = 4
Duplicate found (4 == 4)

Move head until duplicates end:
head moves from first 4 → second 4

Remove duplicate block:
prev.next = head.next
2.next = 5

List becomes:
1 -> 2 -> 5

Move head:
head = 5

---------------------------------------------------------------
Iteration 5:
head = 5
No duplicate
prev = 5
head = None

---------------------------------------------------------------

Final List:
1 -> 2 -> 5

Time Complexity: O(n)
Space Complexity: O(1)

===============================================================
"""