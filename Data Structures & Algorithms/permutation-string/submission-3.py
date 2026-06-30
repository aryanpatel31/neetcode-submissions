class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        window_freq = [0] * 26

        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        l = 0
        r = 0

        while r - l != len(s1):
            window_freq[ord(s2[r]) - ord('a')] += 1
            r += 1

        while r < len(s2):
            if window_freq == s1_freq:
                return True
            else:
                window_freq[ord(s2[r]) - ord('a')] += 1
                window_freq[ord(s2[l]) - ord('a')] -= 1
                r += 1
                l += 1
        
        if window_freq == s1_freq:
                return True
        else:
            return False

            
        

        
            
        




        
        
