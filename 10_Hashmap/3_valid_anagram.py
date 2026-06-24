class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}

        # Count characters of s
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        # Subtract characters using t
        for i in t:
            if i not in freq:
                return False
            else:
                freq[i] -= 1

        # Check if all values are 0
        for i in freq.values():
            if i != 0:
                return False
            
        return True


# Given Input
s = "anagram"
t = "nagaram"

sol = Solution()
print(sol.isAnagram(s, t))

# s = "anagram"
# t = "nagaram"

# Step 1: Length check
# len(s) = 7
# len(t) = 7
# Length equal → continue

# ---------------- COUNT FREQUENCY OF s ----------------

# freq = {}

# 'a' → freq = {'a':1}
# 'n' → freq = {'a':1, 'n':1}
# 'a' → freq = {'a':2, 'n':1}
# 'g' → freq = {'a':2, 'n':1, 'g':1}
# 'r' → freq = {'a':2, 'n':1, 'g':1, 'r':1}
# 'a' → freq = {'a':3, 'n':1, 'g':1, 'r':1}
# 'm' → freq = {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}

# Final freq after s:
# {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}

# ---------------- SUBTRACT USING t ----------------

# 'n' → freq['n'] = 0
# 'a' → freq['a'] = 2
# 'g' → freq['g'] = 0
# 'a' → freq['a'] = 1
# 'r' → freq['r'] = 0
# 'a' → freq['a'] = 0
# 'm' → freq['m'] = 0

# Final freq:
# {'a':0, 'n':0, 'g':0, 'r':0, 'm':0}

# ---------------- CHECK FINAL VALUES ----------------

# All values = 0
# So return True