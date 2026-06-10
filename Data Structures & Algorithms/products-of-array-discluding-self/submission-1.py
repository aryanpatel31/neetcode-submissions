class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(len(nums)):
            pre_product = 1
            suf_product = 1

            for j in range(0, i):
                pre_product *= nums[j]

           
            
            for z in range(len(nums) - 1, i, -1):
                suf_product *= nums[z]
            
            output.append(pre_product * suf_product)
        
        return output
        
        



        

            
            


        