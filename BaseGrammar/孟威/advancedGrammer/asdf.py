"""

"""

import threading
import multiprocessing


grid = [[0,0,0,0,1],[0,4,0,1,0],[0,0,5,0,0],[0,5,0,2,0],[4,0,0,0,2]]

class Solution:
    def checkXMatrix(self, grid):
        grid_len = len(grid)
        for idx, row in enumerate(grid):
            # print(idx, -idx - 1, grid_len - idx - 1)
            if grid[idx][idx] == 0 or grid[idx][grid_len - idx - 1] == 0:
                return False
            if idx == grid_len - idx - 1:
                rowSum = grid[idx][idx]
            else:
                rowSum = grid[idx][idx] + grid[idx][grid_len - idx - 1]
            # print(rowSum, sum(grid[idx]))
            if rowSum != sum(grid[idx]):
                return False
        return True

s = Solution()
print(s.checkXMatrix(grid))