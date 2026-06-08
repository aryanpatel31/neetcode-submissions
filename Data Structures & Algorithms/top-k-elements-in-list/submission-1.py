class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        output = []

        for val in nums:
            counts[val] = 1 + counts.get(val, 0)

        for _ in range(k):
            output.append(max(counts, key = counts.get))
            counts.pop(max(counts, key = counts.get))

        return output
        
        
            

        
        


        
        


        

        
        