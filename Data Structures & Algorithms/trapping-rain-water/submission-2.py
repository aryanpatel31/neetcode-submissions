class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = []
        prefix.append(0)

        suffix = []
        suffix.append(0)

        for i in range(1,len(height)):
            if height[i-1] > prefix[i-1]:
                prefix.append(height[i-1])
            else: 
                prefix.append(prefix[i-1])

        start = 0
        for i in range(len(height) - 2, -1, -1):
            if height[i+1] > suffix[start]:
                suffix.insert(0, height[i+1])
            else:
                suffix.insert(0, suffix[start])
            
        area = 0
        for i in range(len(height)):
            if (min(prefix[i], suffix[i]) - height[i]) > 0:
                area += (min(prefix[i], suffix[i]) - height[i])
        
        return area

            



        



        


        

            
       
            

        



        