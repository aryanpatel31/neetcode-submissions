class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        length = len(digits)

        i = length - 1

        while i >= 0 and (digits[i] + 1 == 10):
            digits[i] = 0
            i -= 1
        
        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] += 1
        
        return digits
        

