class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c.lower() for c in s if c.isalnum()]

        new_s = ''.join(lst)
        
        low = 0
        high = len(new_s) - 1

        while low < high:
            if new_s[low] != new_s[high]:
                return False
            low += 1
            high -= 1

        return True

        