class MinStack:

    def __init__(self):
        self.items = [] 

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append([val, val])
        else:
            minimum = min(self.items[-1][1], val)
            self.items.append([val, minimum])

    def pop(self) -> None:
        if self.items:
           self.items.pop()


    def top(self) -> int:
        if self.items:
          return self.items[-1][0]
        return None

    def getMin(self) -> int:
        if self.items:
            return self.items[-1][1]
        return None

obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())   # -3

obj.pop()

param_3 = obj.top()      # 0
param_4 = obj.getMin()   # -2

print(param_3)
print(param_4)

''' ---------------- DRY RUN ----------------

obj = MinStack()
# items = []

obj.push(-2)
# Stack was empty
# items = [[-2, -2]]

obj.push(0)
# Previous min = -2
# min(-2, 0) = -2
# items = [[-2,-2], [0,-2]]

obj.push(-3)
# Previous min = -2
# min(-2, -3) = -3
# items = [[-2,-2], [0,-2], [-3,-3]]

print(obj.getMin())
# Top min = -3
# Output: -3

obj.pop()
# Remove last element [-3,-3]
# items = [[-2,-2], [0,-2]]

param_3 = obj.top()
# Top value = 0
# param_3 = 0

param_4 = obj.getMin()
# Current min = -2
# param_4 = -2

print(param_3)
print(param_4)'''