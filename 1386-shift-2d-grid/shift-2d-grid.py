from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        # Total number of elements
        total = m * n
        
        # Reduce unnecessary shifts
        k %= total
        
        # Flatten the grid
        arr = []
        for row in grid:
            arr.extend(row)
        
        # Shift elements to the right
        arr = arr[-k:] + arr[:-k] if k else arr
        
        # Convert back to 2D grid
        result = []
        for i in range(m):
            result.append(arr[i * n:(i + 1) * n])
        
        return result