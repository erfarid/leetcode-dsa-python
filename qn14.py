# Input: strs = ["flower","flow","flight"]
# Output: "fl"
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            i = 0  
            while i < len(prefix) and i  < len(s) and prefix[i]==s[i]:
                i+=1

            prefix =prefix[:i]
            if prefix =="":
                return "" 

        return prefix    
               
        
        
sol =Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
