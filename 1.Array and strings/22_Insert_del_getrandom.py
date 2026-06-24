import random


class RandomizedSet:
    def __init__(self):
        self.numMap={}
        self.numList=[]

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val]=len(self.numList)
            self.numList.append(val)
        return res
        
    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        
        idx = self.numMap[val]
        lastval = self.numList[-1]
        self.numList[idx] = lastval
        self.numMap[lastval] = idx
        self.numList.pop()
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
       return random.choice(self.numList)

operations = ["RandomizedSet", "insert", "remove", "insert",
              "getRandom", "remove", "insert", "getRandom"]

values = [[], [1], [2], [2], [], [1], [2], []]

output = []
obj = None

for op, val in zip(operations, values):
    if op == "RandomizedSet":
        obj = RandomizedSet()
        output.append(None)
    elif op == "insert":
        output.append(obj.insert(val[0]))
    elif op == "remove":
        output.append(obj.remove(val[0]))
    elif op == "getRandom":
        output.append(obj.getRandom())

print(output)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""

# =========================
# DRY RUN OF OPERATIONS
# =========================

obj = RandomizedSet()

# 1) insert(1)
# numMap = {1:0}
# numList = [1]
# Output: True
print(obj.insert(1))

# 2) remove(2)
# 2 not in numMap
# numMap = {1:0}
# numList = [1]
# Output: False
print(obj.remove(2))

# 3) insert(2)
# numMap = {1:0, 2:1}
# numList = [1,2]
# Output: True
print(obj.insert(2))

# 4) getRandom()
# Random from [1,2]
# Suppose it returns 2
print(obj.getRandom())

# 5) remove(1)
# idx = 0
# lastval = 2
# numList becomes [2]
# numMap becomes {2:0}
# Output: True
print(obj.remove(1))

# 6) insert(2)
# 2 already exists
# numMap = {2:0}
# numList = [2]
# Output: False
print(obj.insert(2))

# 7) getRandom()
# Only element is 2
print(obj.getRandom())

"""