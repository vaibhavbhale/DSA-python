class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}    
        left = 0
        maximum = 0
        
        for right in range(len(s)):
            if s[right] in dic and dic[s[right]] >= left:
                left = dic[s[right]] + 1
            
            dic[s[right]] = right
            maximum = max(maximum, right - left + 1)
        
        return maximum

print(Solution().lengthOfLongestSubstring(s = "abcabcbb"))