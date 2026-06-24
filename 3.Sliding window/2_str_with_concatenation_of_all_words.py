from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        
        result = []
        for i in range(len(s) - total_len + 1):   
            sub = []
            ele = s[i : i + total_len]
            
            for j in range(0, total_len, word_len):
                sub.append(ele[j : j + word_len])  

            if Counter(sub) == word_count:
                result.append(i)
        
        return result
    
print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))