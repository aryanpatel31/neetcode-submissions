class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        import math

        bits = 0

        for num in nums:
            bits ^= num
        
        return bits