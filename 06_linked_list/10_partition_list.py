from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left_tail = left_dummy
        right_tail = right_dummy

        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next
            head = head.next

        right_tail.next = None
        left_tail.next = right_dummy.next

        return left_dummy.next


# ---------------- INPUT ----------------
arr = [1, 4, 3, 2, 5, 2]
x = 3

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
result = obj.partition(head, x)

# ---------------- PRINT RESULT ----------------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("After Partition:")
printList(result)


"""
=========================== DRY RUN ===========================

Input:
1 -> 4 -> 3 -> 2 -> 5 -> 2
x = 3

We create two dummy lists:
Left list  (values < 3)
Right list (values >= 3)

---------------------------------------------------------------

Step 1:
Node = 1
1 < 3 → goes to LEFT

Left: 1
Right: empty

---------------------------------------------------------------

Step 2:
Node = 4
4 >= 3 → goes to RIGHT

Left: 1
Right: 4

---------------------------------------------------------------

Step 3:
Node = 3
3 >= 3 → goes to RIGHT

Left: 1
Right: 4 -> 3

---------------------------------------------------------------

Step 4:
Node = 2
2 < 3 → goes to LEFT

Left: 1 -> 2
Right: 4 -> 3

---------------------------------------------------------------

Step 5:
Node = 5
5 >= 3 → goes to RIGHT

Left: 1 -> 2
Right: 4 -> 3 -> 5

---------------------------------------------------------------

Step 6:
Node = 2
2 < 3 → goes to LEFT

Left: 1 -> 2 -> 2
Right: 4 -> 3 -> 5

---------------------------------------------------------------

Now connect both lists:

Left tail (2) connects to Right head (4)

Final List:
1 -> 2 -> 2 -> 4 -> 3 -> 5

---------------------------------------------------------------

Final Output:
1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None

Time Complexity: O(n)
Space Complexity: O(1)

===============================================================
"""