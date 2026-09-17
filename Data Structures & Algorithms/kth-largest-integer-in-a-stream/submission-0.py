class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.object = nums
        self.k = k

    def add(self, val: int) -> int:
        self.object.append(val)

        self.object.sort(reverse = True)
        #print(self.object)
        return self.object[self.k - 1]

        
