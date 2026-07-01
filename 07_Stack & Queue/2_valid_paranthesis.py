class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x in '({[':
                   stack.append(x)
            elif x == ')':
                if len(stack) !=0 and stack[-1] == '(':
                   stack.pop()
                else:
                   return False
            elif x =='}':
                if len(stack) !=0 and stack[-1] == '{':
                    stack.pop()
                else:
                   return False 
            elif x ==']':
                if len(stack) !=0 and stack[-1] == '[':
                    stack.pop()
                else:
                   return False 
                 
        return len(stack) == 0

print(Solution().isValid(s = "()[]{}"))


# Iteration 1:
            # x = '('
            # stack = []
            # '(' is opening bracket → push
            # stack = ['(']

            # Iteration 2:
            # x = ')'
            # stack = ['(']
            # stack[-1] == '(' → matches
            # pop()
            # stack = []

            # Iteration 3:
            # x = '['
            # stack = []
            # Opening bracket → push
            # stack = ['[']

            # Iteration 4:
            # x = ']'
            # stack = ['[']
            # stack[-1] == '[' → matches
            # pop()
            # stack = []

            # Iteration 5:
            # x = '{'
            # stack = []
            # Opening bracket → push
            # stack = ['{']

            # Iteration 6:
            # x = '}'
            # stack = ['{']
            # stack[-1] == '{' → matches
            # pop()
            # stack = []

        # Loop finished
        # stack = []
