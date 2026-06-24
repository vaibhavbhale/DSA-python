from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 1
        dummy = head
        
        # Step 1: Find length
        while dummy.next:
            dummy = dummy.next
            length += 1

        # Step 2: Reduce k
        k = k % length
        if k == 0:
            return head

        # Step 3: Make it circular
        dummy.next = head

        # Step 4: Find new tail
        current = head
        i = 1
        while i <= length - k - 1:
            current = current.next
            i += 1

        # Step 5: Break circle
        new_head = current.next
        current.next = None

        return new_head


# ---------------- INPUT ----------------
arr = [1, 2, 3, 4, 5]
k = 2

# Convert list to linked list
def createLinkedList(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

head = createLinkedList(arr)

# ---------------- FUNCTION CALL ----------------
obj = Solution()
result = obj.rotateRight(head, k)

# ---------------- PRINT RESULT ----------------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("After Rotating:")
printList(result)


"""
=========================== DRY RUN ===========================

Input:
1 -> 2 -> 3 -> 4 -> 5
k = 2

---------------------------------------------------------------
Step 1: Find Length

Traverse list:
1 → 2 → 3 → 4 → 5

length = 5
dummy now at node 5

---------------------------------------------------------------
Step 2: Reduce k

k = 2 % 5 = 2

---------------------------------------------------------------
Step 3: Make List Circular

5.next = 1

Now list becomes:
1 → 2 → 3 → 4 → 5
↑_________________|

---------------------------------------------------------------
Step 4: Find New Tail

We move (length - k - 1) steps
= (5 - 2 - 1) = 2 steps

Start at head (1)

Step 1 → 2
Step 2 → 3

current = 3 (new tail)

---------------------------------------------------------------
Step 5: Break Circle

new_head = current.next = 4
current.next = None

Final List:
4 → 5 → 1 → 2 → 3

---------------------------------------------------------------

Final Output:
4 -> 5 -> 1 -> 2 -> 3 -> None

Time Complexity: O(n)
Space Complexity: O(1)

===============================================================
"""