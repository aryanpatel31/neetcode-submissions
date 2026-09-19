import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        heapq.heapify(heap) 

        res = []

        for point in points:
            distance = math.sqrt(((point[0] - 0) ** 2) + ((point[1] - 0) ** 2))
            heapq.heappush(heap, (distance, point))

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        


