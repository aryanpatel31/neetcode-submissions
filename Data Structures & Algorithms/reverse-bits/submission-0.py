class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        bit_mask = 1

        for i in range(32):
            bit = (n >> i) & bit_mask
            if bit:
                (res) |= (bit_mask << (31-i))

        return res

