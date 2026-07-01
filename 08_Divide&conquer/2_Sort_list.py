from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head

        slow = head
        fast = head.next   

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split list into two halves
        mid = slow.next
        slow.next = None   

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge sorted halves
        return self.merge(left, right)


    def merge(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        # Attach remaining nodes
        temp.next = l1 if l1 else l2

        return dummy.next


# ------------------ INPUT ------------------
arr = [-1, 5, 3, 4, 0]

# Convert Python list to Linked List
def createLinkedList(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head


head = createLinkedList(arr)

# ------------------ FUNCTION CALL ------------------
obj = Solution()
sorted_head = obj.sortList(head)

# ------------------ PRINT RESULT ------------------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("Sorted List:")
printList(sorted_head)


"""
====================== DRY RUN ======================

Input:
-1 -> 5 -> 3 -> 4 -> 0

-----------------------------------------------------
STEP 1: First Split

slow at -1
fast at 5

After loop:
slow stops at 3

Split into:
Left  = -1 -> 5 -> 3
Right = 4 -> 0

-----------------------------------------------------
STEP 2: Sort Left (-1 -> 5 -> 3)

Find middle:
slow stops at 5

Split:
Left  = -1 -> 5
Right = 3

Now split (-1 -> 5):

Left  = -1
Right = 5

Merge:
-1 -> 5

Now merge (-1 -> 5) with (3):

Compare:
-1 < 3 → -1
5 > 3  → 3
Remaining → 5

Result:
-1 -> 3 -> 5

-----------------------------------------------------
STEP 3: Sort Right (4 -> 0)

Split:
Left  = 4
Right = 0

Merge:
0 -> 4

-----------------------------------------------------
STEP 4: Final Merge

Left  = -1 -> 3 -> 5
Right = 0 -> 4

Compare step-by-step:

-1 < 0 → -1
3 > 0  → 0
3 < 4  → 3
5 > 4  → 4
Remaining → 5

-----------------------------------------------------
FINAL SORTED LIST:

-1 -> 0 -> 3 -> 4 -> 5

-----------------------------------------------------

Time Complexity: O(n log n)
Space Complexity: O(log n)

=====================================================
"""
