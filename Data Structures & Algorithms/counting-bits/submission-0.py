class Solution:
    def countBits(self, n: int) -> List[int]:
        
        bitmask = 1 

        res = []
        for i in range(n + 1):
            count = 0
            for j in range(32):
                count += ((i >> j) & bitmask)

            res.append(count)
            count = 0

        return res


                