class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0 
        
        if len(s) == 1:
            return 1
        
        l = 0
        r = 0
        res = 0

        chars = set()
        chars.add(s[l])

        while r != len(s) - 1:
            r += 1
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)

        return res
            
            
        

