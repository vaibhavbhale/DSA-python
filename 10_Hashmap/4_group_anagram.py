from typing import List

class Solution:
    def sortstrings(self, s):
        s1 = list(s)
        s1.sort()
        return "".join(s1)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            key = self.sortstrings(s)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        
        return list(hashmap.values())


# Given Input
strs = ["eat","tea","tan","ate","nat","bat"]

sol = Solution()
print(sol.groupAnagrams(strs))

# strs = ["eat","tea","tan","ate","nat","bat"]

# hashmap = {}

# 1) s = "eat"
# sortstrings("eat") → "aet"
# hashmap = {"aet": ["eat"]}

# 2) s = "tea"
# sortstrings("tea") → "aet"
# "aet" already in hashmap
# hashmap = {"aet": ["eat", "tea"]}

# 3) s = "tan"
# sortstrings("tan") → "ant"
# hashmap = {
#   "aet": ["eat", "tea"],
#   "ant": ["tan"]
# }

# 4) s = "ate"
# sortstrings("ate") → "aet"
# hashmap = {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan"]
# }

# 5) s = "nat"
# sortstrings("nat") → "ant"
# hashmap = {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"]
# }

# 6) s = "bat"
# sortstrings("bat") → "abt"
# hashmap = {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }

# Return list(hashmap.values())

# Final Output:
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]