import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        heapq.heapify(heap) 

        res = []

        for point in points:
            distance = math.sqrt(((point[0] - 0) ** 2) + ((point[1] - 0) ** 2))
            if not heap or len(heap) < k or heap[0][0] < -distance:
                if len(heap) >= k:
                    heapq.heappop(heap)
                heapq.heappush(heap, (-distance, point))

        for tup in heap:
            res.append(tup[1])

        return res
        


