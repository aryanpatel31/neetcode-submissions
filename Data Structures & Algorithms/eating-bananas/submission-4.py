class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        K = max(piles)

        low = 1
        high = K

        while low <= high:
            midK = low + ((high - low) // 2)
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / midK)
            if hrs <= h:
                high = midK - 1
                K = midK
            else:
                low = midK + 1

        return K
 

