from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        health -= grid[0][0]

        if health < 1:
            return False 

        # now making matrix containing -1 on each position   
        best_health = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(-1)
            best_health.append(row)    

        best_health[0][0] = health 

        queue = deque()
        
        queue.append((0, 0, health))  
        # queue = [(0, 0, 3)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c, curr_health = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return True

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    new_health = curr_health - grid[new_r][new_c]

                    if new_health >= 1 and new_health > best_health[new_r][new_c]:
                        best_health[new_r][new_c] = new_health
                        queue.append((new_r, new_c, new_health))

        return False