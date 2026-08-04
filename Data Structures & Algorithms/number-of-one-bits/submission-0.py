class Solution:
    def hammingWeight(self, n: int) -> int:
        
        one_count = 0
        for i in range(32):
            one_count += ((n >> i) & 1)

        return one_count
