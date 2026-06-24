class Solution:
    def longestCommonPrefix(self, strs): 
        if len (strs )== 0:
            return ""
        
        base = strs[0]
         # base = "flower"
        for i in range(len(base)):
            for word in strs[1:]:
                if(i == len(word) or word[i]!= base[i]):
                 return base[0 : i]
        return base 

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

            #base[0] = 'f'
            # Compare with:
            #   "flow"[0] = 'f'  ✅
            #   "flight"[0] = 'f' ✅
            # No mismatch
            
            # ---- i = 1 ----
            # base[1] = 'l'
            #   "flow"[1] = 'l'  ✅
            #   "flight"[1] = 'l' ✅
            # No mismatch
            
            # ---- i = 2 ----
            # base[2] = 'o'
            #   "flow"[2] = 'o'  ✅
            #   "flight"[2] = 'i' ❌ mismatch
            
            # Since mismatch found at i = 2
            # return base[0:2] → "fl