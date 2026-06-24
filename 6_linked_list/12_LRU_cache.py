class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            val = self.dict[key]
            del self.dict[key]        # remove old position
            self.dict[key] = val      # insert at end (most recently used)
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            del self.dict[key]
            self.dict[key] = value
        else:
            if len(self.dict) < self.capacity:
                self.dict[key] = value
            else:
                # remove least recently used (first key)
                del self.dict[list(self.dict)[0]]
                self.dict[key] = value


# ---------------- INPUT ----------------

operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

output = []

for i in range(len(operations)):
    if operations[i] == "LRUCache":
        obj = LRUCache(values[i][0])
        output.append(None)

    elif operations[i] == "put":
        obj.put(values[i][0], values[i][1])
        output.append(None)

    elif operations[i] == "get":
        result = obj.get(values[i][0])
        output.append(result)

print("Output:", output)


"""
=========================== DRY RUN ===========================

Operations:

1) LRUCache(2)
Capacity = 2
Cache = {}

---------------------------------------------------------------

2) put(1,1)
Cache = {1:1}

---------------------------------------------------------------

3) put(2,2)
Cache = {1:1, 2:2}

---------------------------------------------------------------

4) get(1)
1 exists

Move 1 to most recent:
Remove 1 → {2:2}
Insert 1 → {2:2, 1:1}

Return 1

---------------------------------------------------------------

5) put(3,3)

Cache is full (size=2)

Remove least recently used
LRU = 2 (first key)

Delete 2 → {1:1}
Insert 3 → {1:1, 3:3}

---------------------------------------------------------------

6) get(2)
2 not present
Return -1

---------------------------------------------------------------

7) put(4,4)

Cache full again

LRU = 1

Delete 1 → {3:3}
Insert 4 → {3:3, 4:4}

---------------------------------------------------------------

8) get(1)
Not present
Return -1

---------------------------------------------------------------

9) get(3)
Exists

Move 3 to most recent:
Remove 3 → {4:4}
Insert 3 → {4:4, 3:3}

Return 3

---------------------------------------------------------------

10) get(4)
Exists

Move 4 to most recent:
Remove 4 → {3:3}
Insert 4 → {3:3, 4:4}

Return 4

---------------------------------------------------------------

Final Output:
[None, None, None, 1, None, -1, None, -1, 3, 4]

Time Complexity:
get()  → O(1)
put()  → O(1)

===============================================================
"""