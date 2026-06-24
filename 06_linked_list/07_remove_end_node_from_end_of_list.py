from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head

        # Move p2 n steps ahead
        for i in range(n):
            p2 = p2.next

        # If p2 becomes None → remove head
        if p2 == None:
            head = head.next
            return head
        
        # Move both pointers
        while p2.next != None:
            p2 = p2.next
            p1 = p1.next
        
        # Remove nth node
        p1.next = p1.next.next

        return head


# ---------------- INPUT ----------------
arr = [1, 2, 3, 4, 5]
n = 2

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
result = obj.removeNthFromEnd(head, n)

# ---------------- PRINT RESULT ----------------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("After Removing Nth Node From End:")
printList(result)


"""
========================= DRY RUN =========================

Input:
1 -> 2 -> 3 -> 4 -> 5
n = 2

We need to remove 2nd node from end.
2nd from end = 4

-----------------------------------------------------------
STEP 1: Initialize
p1 = 1
p2 = 1

-----------------------------------------------------------
STEP 2: Move p2 n steps ahead

Move 1 step → p2 = 2
Move 2 step → p2 = 3

Now:
p1 = 1
p2 = 3

Distance between p1 and p2 = 2 nodes

-----------------------------------------------------------
STEP 3: Move both until p2.next == None

Iteration 1:
p2 = 4
p1 = 2

Iteration 2:
p2 = 5
p1 = 3

Now p2.next == None → stop

p1 is at node 3
p1.next is node 4 (target)

-----------------------------------------------------------
STEP 4: Remove node

p1.next = p1.next.next

3.next = 5

List becomes:
1 -> 2 -> 3 -> 5

-----------------------------------------------------------

FINAL OUTPUT:
1 -> 2 -> 3 -> 5

Time Complexity: O(n)
Space Complexity: O(1)

===========================================================
"""