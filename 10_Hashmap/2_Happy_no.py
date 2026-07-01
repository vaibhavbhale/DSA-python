class Solution:
    def isHappy(self, n: int) -> bool:    
        visit = set()
        
        def get_next_number(n):    
            output = 0
            
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output

        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        
        return False


# Given Input
n = 19

sol = Solution()
print(sol.isHappy(n))

# n = 19
# visit = {}

# ---------------- FIRST ITERATION ----------------
# n = 19 (not in visit)
# visit = {19}

# get_next_number(19)
# digits: 1^2 + 9^2
# = 1 + 81
# = 82
# n = 82

# ---------------- SECOND ITERATION ----------------
# n = 82 (not in visit)
# visit = {19, 82}

# get_next_number(82)
# digits: 8^2 + 2^2
# = 64 + 4
# = 68
# n = 68

# ---------------- THIRD ITERATION ----------------
# n = 68 (not in visit)
# visit = {19, 82, 68}

# get_next_number(68)
# digits: 6^2 + 8^2
# = 36 + 64
# = 100
# n = 100

# ---------------- FOURTH ITERATION ----------------
# n = 100 (not in visit)
# visit = {19, 82, 68, 100}

# get_next_number(100)
# digits: 1^2 + 0^2 + 0^2
# = 1 + 0 + 0
# = 1
# n = 1

# Since n == 1 → return True