class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        bitset = 0

        for num in nums:
            bitset |= (1 << num)

        bitmask = 1

        for i in range(len(nums)):
            if not (bitmask & (bitset >> i)):
                return i

        return len(nums)

