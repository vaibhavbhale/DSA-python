class Solution:
    def calculate(self, s: str) -> int:
        operation = 1
        number = 0
        stack = []
        output = 0
        i =0
        
        while i < len(s):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
           
            elif s[i] == '+':
                output += operation * number
                number = 0
                operation = 1
            
            elif s[i] == '-':
                output += operation * number
                number = 0
                operation = -1
            
            elif s[i] == '(':
                stack.append(output)
                stack.append(operation)
                output = 0
                operation = 1
            
            elif s[i] == ')':
                output += operation * number
                number = 0
                
                prev_operation = stack.pop()
                prev_output = stack.pop()
                
                output = prev_output + prev_operation * output
            
            i += 1
        
        output += operation * number
        return output


print(Solution().calculate(s = "(1+(4+5+2)-3)+(6+8)"))



            # i=0 → '('
            # Push current output and operation
            # stack = [0, 1]
            # Reset output=0, operation=1

            # i=1 → '1'
            # number = 1

            # i=2 → '+'
            # output += 1*1 = 1
            # number = 0
            # operation = 1

            # i=3 → '('
            # Push current output and operation
            # stack = [0,1,1,1]
            # Reset output=0, operation=1

            # i=4 → '4'
            # number = 4

            # i=5 → '+'
            # output += 1*4 = 4
            # number = 0

            # i=6 → '5'
            # number = 5

            # i=7 → '+'
            # output += 1*5 = 9
            # number = 0

            # i=8 → '2'
            # number = 2

            # i=9 → ')'
            # output += 1*2 = 11
            # number = 0
            # prev_operation = 1
            # prev_output = 1
            # output = 1 + 1*11 = 12
            # stack = [0,1]

            # i=10 → '-'
            # output += 1*0 = 12
            # operation = -1

            # i=11 → '3'
            # number = 3

            # i=12 → ')'
            # output += (-1)*3 = 9
            # number = 0
            # prev_operation = 1
            # prev_output = 0
            # output = 0 + 1*9 = 9
            # stack = []

            # i=13 → '+'
            # output = 9
            # operation = 1

            # i=14 → '('
            # stack = [9,1]
            # output=0, operation=1

            # i=15 → '6'
            # number = 6

            # i=16 → '+'
            # output += 6 = 6
            # number = 0

            # i=17 → '8'
            # number = 8

            # i=18 → ')'
            # output += 8 = 14
            # prev_operation = 1
            # prev_output = 9
            # output = 9 + 1*14 = 23
            # stack = []
