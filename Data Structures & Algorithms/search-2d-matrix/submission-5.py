class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if target < matrix[0][0]:
            return False

        #two binary search, one on first col, then in the row
        low = 0 
        high = len(matrix) - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1         
            else:
                high = mid - 1
            
        row = high
        low = 0
        high = len(matrix[0]) - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False