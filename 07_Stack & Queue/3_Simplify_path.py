class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []
       
        for dir in dirs:
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(dir)
        
        return '/' + '/'.join(stack)
    
print(Solution().simplifyPath("/home//foo/"))



            # 1️⃣ dir = ""
            # Empty because path starts with '/'
            # Condition: dir == '' → continue
            # stack = []

            # 2️⃣ dir = "home"
            # Not empty, not '.', not '..'
            # stack.append("home")
            # stack = ["home"]

            # 3️⃣ dir = ""
            # Empty because of "//"
            # continue
            # stack = ["home"]

            # 4️⃣ dir = "foo"
            # Normal folder → append
            # stack = ["home", "foo"]

            # 5️⃣ dir = ""
            # Empty because path ends with '/'
            # continue
            # stack = ["home", "foo"]

            
        # After loop:
        # stack = ["home", "foo"]

        # "/" + "home/foo"
        # Final result = "/home/foo"
