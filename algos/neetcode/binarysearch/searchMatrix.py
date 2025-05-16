#https://neetcode.io/problems/search-2d-matrix class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   

        topRow = 0
        bottomRow = len(matrix)-1

        if(len(matrix)) == 1:
            middleRow = 0
        else:
            while topRow <= bottomRow:
                middleRow = (topRow + bottomRow) // 2
                if matrix[middleRow][0] <= target <= matrix[middleRow][-1]:
                    # Target is in this row
                    break
                elif matrix[middleRow][0] < target:
                    topRow = middleRow + 1
                else:
                    bottomRow = middleRow - 1

        
        # If no row is found
        if topRow > bottomRow:
            return False
        
        l,r= 0, len(matrix[0])
        while l<r:
            m =(l+r) // 2
            if target == matrix[middleRow][m]:
                return True
            if target >  matrix[middleRow][m]:
                l = l + 1
            else:
                r = r - 1
        return False
