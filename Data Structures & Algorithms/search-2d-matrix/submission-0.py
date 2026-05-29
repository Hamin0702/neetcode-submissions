class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        leftRow = 0
        rightRow = ROWS - 1

        while(leftRow <= rightRow):
            midRow = (leftRow + rightRow) // 2
            
            if matrix[midRow][0] > target:
                rightRow = midRow - 1
            elif matrix[midRow][-1] < target:
                leftRow = midRow + 1
            else:
                break

        if not (leftRow <= rightRow):
            return False

        targetRow = (leftRow + rightRow) // 2
        left = 0
        right = COLS - 1

        while(left <= right):
            mid = (left + right) // 2
            
            if matrix[targetRow][mid] > target:
                right = mid - 1
            elif matrix[targetRow][mid] < target:
                left = mid + 1
            else:
                return True

        return False

