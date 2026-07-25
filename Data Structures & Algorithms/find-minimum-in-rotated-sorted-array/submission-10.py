class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1
        res = nums[0]
   

        while l <= r:
             mid = l + ((r - l) // 2)
             res = min(res, nums[mid])
             if nums[l] < nums[r]:
                return min(res, nums[l])
             elif nums[l] <= nums[mid]:
                l =  mid + 1
             else:
                r = mid -1
        
        return res
            




            
    
        
        