from collections import Counter
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        min_len = n + 1
        min_str = ""

        freq = Counter(t)   
        l = 0
        required = len(freq)   
        match = 0

        for r in range(n):
            if s[r] in freq:
                freq[s[r]] -= 1
                if freq[s[r]] == 0:
                    match += 1
            
            while match == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_str = s[l:r+1]
                
                if s[l] in freq:
                    if freq[s[l]] == 0:
                        match -= 1
                    freq[s[l]] += 1
                l += 1
        
        return min_str
s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s,t))
   
"""
        # ------------------------------------------
        # STEP 1: Initial Setup
        # ------------------------------------------
        
        n = len(s)              # Length of string s
        min_len = n + 1         # Store minimum window length found
        min_str = ""            # Store final smallest substring
        
        # Create frequency map of characters in t
        # Example: t = "ABC"
        # freq = {'A':1, 'B':1, 'C':1}
        freq = Counter(t)
        
        l = 0                   # Left pointer
        required = len(freq)    # Number of unique characters needed
        match = 0               # Number of characters fully matched
        
        # ------------------------------------------
        # DRY RUN EXAMPLE
        # s = "ADOBECODEBANC"
        # t = "ABC"
        #
        # freq = {A:1, B:1, C:1}
        # required = 3
        # match = 0
        # l = 0
        # ------------------------------------------
        
        # ------------------------------------------
        # STEP 2: Expand Window using Right Pointer
        # ------------------------------------------
        
        for r in range(n):
            
            # If current character is required
            if s[r] in freq:
                freq[s[r]] -= 1
                
                # If character requirement completed
                if freq[s[r]] == 0:
                    match += 1
            
            # --------------------------------------
            # DRY RUN TRACE
            # --------------------------------------
            # r = 0 → 'A'
            # freq[A] = 0 → match = 1
            #
            # r = 3 → 'B'
            # freq[B] = 0 → match = 2
            #
            # r = 5 → 'C'
            # freq[C] = 0 → match = 3
            #
            # Now match == required (3)
            # Valid window found: "ADOBEC"
            # --------------------------------------
            
            # --------------------------------------
            # STEP 3: Shrink Window
            # --------------------------------------
            
            while match == required:
                
                # Update minimum window
                window_size = r - l + 1
                if window_size < min_len:
                    min_len = window_size
                    min_str = s[l:r+1]
                
                # ----------------------------------
                # First valid window:
                # "ADOBEC" → length 6
                # min_len = 6
                # min_str = "ADOBEC"
                # ----------------------------------
                
                # Try removing left character
                if s[l] in freq:
                    
                    # If removing breaks validity
                    if freq[s[l]] == 0:
                        match -= 1
                    
                    freq[s[l]] += 1
                
                l += 1   # Move left pointer
                
                # ----------------------------------
                # After removing 'A':
                # freq[A] becomes 1
                # match = 2
                # Window invalid again
                # ----------------------------------
        
        # ------------------------------------------
        # Later in traversal:
        #
        # At r = 12:
        # Window becomes "BANC"
        #
        # freq = {A:0, B:0, C:0}
        # match = 3
        #
        # Shrink further:
        # Final smallest window = "BANC"
        # length = 4
        # ------------------------------------------
        
        return min_str


# ==========================================
# FINAL RESULT FOR:
# s = "ADOBECODEBANC"
# t = "ABC"
#
# Output: "BANC"
# ==========================================
"""