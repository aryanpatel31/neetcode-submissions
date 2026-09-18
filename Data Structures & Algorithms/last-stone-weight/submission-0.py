import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = list(map(lambda x : -x, stones))
        
        heapq.heapify(heap) #min heap by default, but all values being negative makes it behave as a max heap

        while len(heap) > 1:
            stone1_weight = heapq.heappop(heap) * -1
            stone2_weight = heapq.heappop(heap) * -1

            if stone1_weight == stone2_weight:
                continue
            else:
                stone1_new_weight = stone1_weight - stone2_weight
                heapq.heappush(heap, (stone1_new_weight) * -1)

        if len(heap) == 1:
            return heapq.heappop(heap) * -1
        else:
            return 0

        