from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+","-","*","/"]

        for c in tokens:
            if c in op:
                a = stack.pop()
                b = stack.pop()

                if c == "+":
                    stack.append(b + a)
                elif c == "-":
                    stack.append(b - a)
                elif c == "*":
                    stack.append(b * a)
                elif c == "/":
                    stack.append(int(b / a))   
            else:
                stack.append(int(c))

        return stack[-1]


print(Solution().evalRPN(["2","1","+","3","*"]))


  # -------- Iteration 1 --------
            # c = "2"
            # Not an operator
            # stack.append(2)
            # stack = [2]

            # -------- Iteration 2 --------
            # c = "1"
            # Not an operator
            # stack.append(1)
            # stack = [2, 1]

            # -------- Iteration 3 --------
            # c = "+"
            # Operator found
            # a = stack.pop() → 1
            # b = stack.pop() → 2
            # Compute b + a = 2 + 1 = 3
            # stack = [3]

            # -------- Iteration 4 --------
            # c = "3"
            # Not an operator
            # stack.append(3)
            # stack = [3, 3]

            # -------- Iteration 5 --------
            # c = "*"
            # Operator found
            # a = stack.pop() → 3
            # b = stack.pop() → 3
            # Compute b * a = 3 * 3 = 9
            # stack = [9]
