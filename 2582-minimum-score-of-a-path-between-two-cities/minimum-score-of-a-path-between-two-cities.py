from typing import List
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build undirected graph
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = set()
        queue = deque([1])
        visited.add(1)

        ans = float("inf")

        # Visit all cities connected to city 1
        while queue:
            city = queue.popleft()

            for nei, distance in graph[city]:
                ans = min(ans, distance)

                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return ans