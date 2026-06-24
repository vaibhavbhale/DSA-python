from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0) 
        root = head
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1+v2+carry

            carry = s//10 
            head.next=ListNode(s % 10)
            head = head.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        if carry:
            head.next =  ListNode(carry)
        
        return root.next
    
def createLinkedList(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def printLinkedList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


l1_input = [2, 4, 3]
l2_input = [5, 6, 4]

l1 = createLinkedList(l1_input)
l2 = createLinkedList(l2_input)

# Solve
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Output
print("Result Linked List:")
printLinkedList(result)

   # -------- Iteration 1 --------
            # v1 = 2
            # v2 = 5
            # carry = 0
            # sum = 2 + 5 + 0 = 7
            # new digit = 7 % 10 = 7
            # new carry = 7 // 10 = 0
            
            # -------- Iteration 2 --------
            # v1 = 4
            # v2 = 6
            # carry = 0
            # sum = 4 + 6 + 0 = 10
            # new digit = 10 % 10 = 0
            # new carry = 10 // 10 = 1
            
            # -------- Iteration 3 --------
            # v1 = 3
            # v2 = 4
            # carry = 1
            # sum = 3 + 4 + 1 = 8
            # new digit = 8 % 10 = 8
            # new carry = 8 // 10 = 0