from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        m = {}
        new_head = Node(head.val)
        m[head] = new_head

        old_temp = head.next
        new_temp = new_head

        while old_temp:
            copy_node = Node(old_temp.val)
            m[old_temp] = copy_node
            new_temp.next = copy_node

            old_temp = old_temp.next
            new_temp = new_temp.next
            
        old_temp = head
        new_temp = new_head

        while old_temp:
            if old_temp.random:
                new_temp.random = m[old_temp.random]
            else:
                new_temp.random = None

            old_temp = old_temp.next
            new_temp = new_temp.next

        return new_head

def buildLinkedList(arr):
    if not arr:
        return None

    nodes = [Node(val) for val, _ in arr]

    # Connect next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Connect random pointers
    for i, (_, rand_index) in enumerate(arr):
        if rand_index is not None:
            nodes[i].random = nodes[rand_index]

    return nodes[0]


# 🔹 Print list in same format
def printList(head):
    result = []
    index_map = {}

    temp = head
    idx = 0
    while temp:
        index_map[temp] = idx
        temp = temp.next
        idx += 1

    temp = head
    while temp:
        rand_index = index_map[temp.random] if temp.random else None
        result.append([temp.val, rand_index])
        temp = temp.next

    print(result)

head_input = [[7,None],[13,0],[11,4],[10,2],[1,0]]

# Build original list
head = buildLinkedList(head_input)

# Copy list
solution = Solution()
copied_head = solution.copyRandomList(head)

# Output
print("Copied List:")
printList(copied_head)

# Input:
# head = [[7,None],[13,0],[11,4],[10,2],[1,0]]

# FIRST PASS (Copy nodes and next pointers)

# Step 1:
# Create copy of node 7
# Map original(7) → copy(7)

# Step 2:
# Create copy of node 13
# Link copy: 7 → 13
# Map original(13) → copy(13)

# Step 3:
# Create copy of node 11
# Link copy: 7 → 13 → 11
# Map original(11) → copy(11)

# Step 4:
# Create copy of node 10
# Link copy: 7 → 13 → 11 → 10
# Map original(10) → copy(10)

# Step 5:
# Create copy of node 1
# Link copy: 7 → 13 → 11 → 10 → 1
# Map original(1) → copy(1)

# At this stage:
# Copied list (only next pointers set):
# 7 → 13 → 11 → 10 → 1
# Random pointers NOT set yet


# SECOND PASS (Set random pointers using hashmap)

# Node 7:
# original random = None
# copy random = None

# Node 13:
# original random → node 7
# copy random → copy(7)

# Node 11:
# original random → node 1
# copy random → copy(1)

# Node 10:
# original random → node 11
# copy random → copy(11)

# Node 1:
# original random → node 7
# copy random → copy(7)

# Final copied list:
# [[7,None],[13,0],[11,4],[10,2],[1,0]]