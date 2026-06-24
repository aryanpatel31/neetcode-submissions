class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        my_set = {s[0]}

        left = 0
        right = 1
        res = 0
        

        while right < len(s):
            if s[right] in my_set:
                res = max(res, right - left)
                while s[left] != s[right]:
                    my_set.remove(s[left])
                    left += 1
                my_set.remove(s[left])
                left += 1
            else:
                my_set.add(s[right])
                right += 1
        
        res = max(res, right - left)
        return res