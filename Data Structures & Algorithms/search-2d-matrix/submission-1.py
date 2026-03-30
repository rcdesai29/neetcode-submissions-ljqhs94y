class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1

        while top<= bottom:
            mid = (top+bottom)//2
            
            if matrix[mid][-1] < target:
                top = mid+1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        
        if(bottom < top):
            return False
        
        row = (top+bottom) //2
        l = 0 
        r = cols-1
        while l<=r:
            mid = (l+r)//2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid -1
            else:
                return True
        return False
        
            