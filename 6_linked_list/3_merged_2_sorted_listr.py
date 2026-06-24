from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        head = res

        while list1 and list2:
            if list1 and list2:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next
    
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        
        return res.next

def createLinkedList(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# 🔹 Print linked list
def printLinkedList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

list1 = [1,2,4], 
list2 = [1,3,4]

list1 = createLinkedList(list1)
list2 = createLinkedList(list2)

# Merge
solution = Solution()
result = solution.mergeTwoLists(list1, list2)

# Output
print("Merged Linked List:")
printLinkedList(result)

# ---- Iteration 1 ----
            # list1.val = 1
            # list2.val = 1
            # 1 <= 1 → True
            # Attach list1 node
            # result: 1
            # list1 moves to 2
            
            # ---- Iteration 2 ----
            # list1.val = 2
            # list2.val = 1
            # 2 <= 1 → False
            # Attach list2 node
            # result: 1 -> 1
            # list2 moves to 3
            
            # ---- Iteration 3 ----
            # list1.val = 2
            # list2.val = 3
            # 2 <= 3 → True
            # Attach list1
            # result: 1 -> 1 -> 2
            # list1 moves to 4
            
            # ---- Iteration 4 ----
            # list1.val = 4
            # list2.val = 3
            # 4 <= 3 → False
            # Attach list2
            # result: 1 -> 1 -> 2 -> 3
            # list2 moves to 4
            
            # ---- Iteration 5 ----
            # list1.val = 4
            # list2.val = 4
            # 4 <= 4 → True
            # Attach list1
            # result: 1 -> 1 -> 2 -> 3 -> 4
            # list1 becomes None

        
        # After loop:
        # list1 = None
        # list2 = 4
        
        # Attach remaining list2
        
        # Final merged list:
        # 1 -> 1 -> 2 -> 3 -> 4 -> 4