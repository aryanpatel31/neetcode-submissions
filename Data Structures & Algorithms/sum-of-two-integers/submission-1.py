class Solution:
    def getSum(self, a: int, b: int) -> int:

        res = 0
        carry = 0

        MASK = 0xFFFFFFFF

        # treat a and b as 32-bit unsigned numbers
        a &= MASK
        b &= MASK

        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1

            # full adder
            total = abit + bbit + carry

            if total % 2:
                res |= (1 << i)

            carry = total // 2

        # convert 32 bit unsigned result back to signed integer
        if res > 0x7FFFFFFF:
            res -= 0x100000000

        return res
            
            

            

            
            


        