class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqs = [0] * 26

        l = 0
        res = 0
        
        
        for r in range(len(s)):
            window_len = r - l + 1
            freqs[ord(s[r]) - ord('A')] += 1
            if window_len - max(freqs) <= k:
                res = max(res, r - l + 1)
            else:
                while window_len - max(freqs) > k:
                    freqs[ord(s[l]) - ord('A')] -= 1
                    l += 1
                    window_len = r - l + 1

        return max(res, r - l + 1)






            


        