#https://leetcode.com/problems/rotting-oranges/ 

import copy

class Solution:

    def isIsolated(self, i, j , grid):
        if i-1>=0 and grid[i-1][j] != 0:
            return False
        if j-1>=0 and grid[i][j-1] != 0:
            return False
        if i+1<len(grid) and grid[i+1][j] != 0:
            return False
        if j+1<len(grid[0]) and grid[i][j+1] != 0:   
            return False
        return True


    def orangesRotting(self, grid: List[List[int]]) -> int:

        freshOranges = []
        rottenOranges = []
        isIsolated = False

        for row in range(0, len(grid)):
            for column in range(0, len(grid[0])):
                if grid[row][column] == 2:                       
                    rottenOranges.append((row,column))
                elif grid[row][column] == 1:
                    freshOranges.append((row,column))
                    #check if orange is isolated
                    if self.isIsolated(row, column, grid):
                        isIsolated = True
        if len(freshOranges) == 0:
            return 0
        if isIsolated:
            return -1
        if len(rottenOranges) == 0:
            return -1

        freshOrangesMap = {}

        for orange in freshOranges:
            freshOrangesMap[str(orange[0]) + '|' + str(orange[1])] = ''

        newlyRottens = []
        minutes = -1
        while True and len(freshOrangesMap) > 0:
            if minutes == -1:
                listToLoop = rottenOranges
            else:
                listToLoop = copy.deepcopy(newlyRottens)
                newlyRottens = []
            if len(listToLoop) ==0:
                break;
            minutes+=1
            for rotten in listToLoop:
                rottenX = rotten[0]
                rottenY = rotten[1]
                
                if rottenX+1 < len(grid) and str(rottenX+1)+ '|' + str(rottenY) in freshOrangesMap:
                    newlyRottens.append((rottenX+1,rottenY))
                    del freshOrangesMap[str(rottenX+1)+ '|' + str(rottenY)]
                if rottenY+1 < len(grid[0]) and str(rottenX)+ '|' + str(rottenY+1) in freshOrangesMap:
                    newlyRottens.append((rottenX,rottenY+1))
                    del freshOrangesMap[str(rottenX)+ '|' + str(rottenY+1)]
                if rottenX-1 >= 0 and str(rottenX-1)+ '|' + str(rottenY) in freshOrangesMap:
                    newlyRottens.append((rottenX-1,rottenY))
                    del freshOrangesMap[str(rottenX-1)+ '|' + str(rottenY)]
                if rottenY-1 >= 0 and str(rottenX)+ '|' + str(rottenY-1) in freshOrangesMap:
                    newlyRottens.append((rottenX,rottenY-1))
                    del freshOrangesMap[str(rottenX)+ '|' + str(rottenY-1)]

        return minutes+1 if len(freshOrangesMap) == 0 else -1
                        