class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(x)

        while len(self.stack2) > 0:   
            self.stack1.append(self.stack2.pop())
    
    def pop(self) -> int:
        x  = self.stack1[-1]
        self.stack1.pop()
        return x

    def peek(self) -> int:
        return  self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0

obj = MyQueue()

obj.push(1)
obj.push(2)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)

'''
# ---------------- DRY RUN ----------------

obj = MyQueue()
# stack1 = []
# stack2 = []

obj.push(1)
# stack1 was empty → nothing moved
# Insert 1
# stack1 = [1]
# stack2 = []

obj.push(2)
# Move stack1 → stack2
# stack1 = []
# stack2 = [1]
# Insert 2
# stack1 = [2]
# Move back stack2 → stack1
# stack1 = [2, 1]
# stack2 = []

param_2 = obj.pop()
# Remove top element (1)
# stack1 = [2]
# param_2 = 1

param_3 = obj.peek()
# Top element = 2
# stack1 = [2]
# param_3 = 2

param_4 = obj.empty()
# stack1 not empty
# param_4 = False'''