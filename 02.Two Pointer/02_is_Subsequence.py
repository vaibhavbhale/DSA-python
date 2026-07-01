class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        if len(s) == 0:
            return True

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                j+=1
            else:
                j+=1
                i+=1
        
            if i == len(s):
                return True
        return False

s = "abc", t = "ahbgdc"
print(Solution().isSubsequence(s,t))

    
      # Iteration 1:
            # s[i] = 'a'
            # t[j] = 'a'
            # Match → move both
            # i = 1, j = 1

            # Iteration 2:
            # s[i] = 'b'
            # t[j] = 'h'
            # Not match → move j
            # i = 1, j = 2

            # Iteration 3:
            # s[i] = 'b'
            # t[j] = 'b'
            # Match → move both
            # i = 2, j = 3

            # Iteration 4:
            # s[i] = 'c'
            # t[j] = 'g'
            # Not match → move j
            # i = 2, j = 4

            # Iteration 5:
            # s[i] = 'c'
            # t[j] = 'd'
            # Not match → move j
            # i = 2, j = 5

            # Iteration 6:
            # s[i] = 'c'
            # t[j] = 'c'
            # Match → move both
             # i = 3, j = 6