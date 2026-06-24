class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = s.split()
        if (len(str) == 0):
            return 0
        return len(str[-1])

s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))