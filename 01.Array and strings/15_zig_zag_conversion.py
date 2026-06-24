class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Step 1: Create zigzag pattern index list
        # range(3) → [0,1,2]
        # range(1,0,-1) → [1]
        # So t = [0,1,2,1]
        t = list(range(numRows)) + list(range(numRows - 2 , 0 ,-1))
        
        # Step 2: Create empty rows
        # r = ["", "", ""]
        
        r = [''] * numRows
        for i,char in enumerate(s):
            r[t[i % len(t)]] += char
        return ''.join(r)





 # i % len(t) gives position inside zigzag cycle
            # len(t) = 4
            # pattern repeats every 4 characters
            
            # DRY RUN TABLE:
            #
            # i   char   i%4   t[i%4]   Row Updated
            # ---------------------------------------
            # 0    P      0      0      r[0] = "P"
            # 1    A      1      1      r[1] = "A"
            # 2    Y      2      2      r[2] = "Y"
            # 3    P      3      1      r[1] = "AP"
            # 4    A      0      0      r[0] = "PA"
            # 5    L      1      1      r[1] = "APL"
            # 6    I      2      2      r[2] = "YI"
            # 7    S      3      1      r[1] = "APLS"
            # 8    H      0      0      r[0] = "PAH"
            # 9    I      1      1      r[1] = "APLSI"
            # 10   R      2      2      r[2] = "YIR"
            # 11   I      3      1      r[1] = "APLSII"
            # 12   N      0      0      r[0] = "PAHN"
            
        # Final rows:
        # r[0] = "PAHN"
        # r[1] = "APLSIIG"
        # r[2] = "YIR"