class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        area = 0
        
        while l < r:
            new_area = (r-l) * min(heights[l], heights[r])
            if new_area > area:
                area = new_area
            
            if min(heights[l], heights[r]) == heights[l]:
                l += 1
            else:
                r -= 1
            
        return area


        