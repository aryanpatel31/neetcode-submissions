class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        

        for index in range(len(nums) -1) :

            if index > 0 and nums[index] == nums[index-1]:
                continue

            low = index + 1
            high = len(nums) - 1

            while low < high:
                if nums[low] + nums[high] == -(nums[index]):
                    res.append([nums[low], nums[high], nums[index]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                        
                elif nums[low] + nums[high] < -(nums[index]):
                    low += 1
                elif nums[low] + nums[high] > -(nums[index]):
                    high -= 1
            
        return res
                

                


        
            



            

