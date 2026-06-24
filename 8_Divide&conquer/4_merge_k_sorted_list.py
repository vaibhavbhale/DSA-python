from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                
                mergedLists.append(self.merge(l1, l2))
            
            lists = mergedLists
        
        return lists[0]

    
    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
    
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next


# ---------------- INPUT ----------------
input_lists = [[1,4,5],[1,3,4],[2,6]]

# Convert list of lists into linked lists
def createLinkedList(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

lists = [createLinkedList(lst) for lst in input_lists]

# ---------------- FUNCTION CALL ----------------
obj = Solution()
result = obj.mergeKLists(lists)

# ---------------- PRINT RESULT ----------------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("Merged K Lists:")
printList(result)


"""
======================== DRY RUN ========================

Input:
lists = [[1,4,5], [1,3,4], [2,6]]

Converted to linked lists:
L1: 1 -> 4 -> 5
L2: 1 -> 3 -> 4
L3: 2 -> 6

---------------------------------------------------------
STEP 1: First While Loop (len = 3)

Pair 1:
Merge L1 and L2

Compare step-by-step:

1 == 1 → take second 1
1 -> 1
4 > 3 → take 3
1 -> 1 -> 3
4 == 4 → take second 4
1 -> 1 -> 3 -> 4
5 > 4 → take 4
1 -> 1 -> 3 -> 4 -> 4
Remaining 5

Result:
1 -> 1 -> 3 -> 4 -> 4 -> 5

Pair 2:
Merge L3 and None

Result:
2 -> 6

Now lists becomes:
[
  1 -> 1 -> 3 -> 4 -> 4 -> 5,
  2 -> 6
]

---------------------------------------------------------
STEP 2: Second While Loop (len = 2)

Merge both lists:

Compare:

1 < 2 → 1
1 < 2 → 1
3 > 2 → 2
3 < 6 → 3
4 < 6 → 4
4 < 6 → 4
5 < 6 → 5
Remaining → 6

Final Result:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

---------------------------------------------------------

Final Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Time Complexity: O(N log k)
Where:
N = total nodes
k = number of lists

Space Complexity: O(1) (excluding recursion)

=========================================================
"""