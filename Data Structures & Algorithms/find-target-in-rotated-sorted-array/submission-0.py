class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #first find the index of the min of arrray
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + ((r-l)//2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
            
        pivot = l

        #finding which of two segments to search

        if target == nums[pivot]:
            return pivot

        if nums[-1] < target:
            l = 0
            r = pivot -1
        else:
            l = pivot + 1
            r = len(nums) - 1
    

        #then do binary search on the right segment to find the target

        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1



        
        
        
            