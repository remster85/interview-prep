#https://leetcode.com/problems/number-of-islands/
class Solution:

    def dfs(self, i, j, grid:  List[List[str]]):

        n = len(grid[0])
        m = len(grid)

        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'

        self.dfs(i + 1, j, grid)
        self.dfs(i - 1, j, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i, j - 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid[0])
        m = len(grid)

        if m == 0 or n == 0:
            return 0
                
        numberOfIslands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    numberOfIslands +=1
                    self.dfs(i , j , grid)

        return numberOfIslands 


