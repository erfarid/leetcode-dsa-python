from typing import List
from collections import deque
import math

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        # Build graph and topological order because graph is DAG
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        max_cost = 0
        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            max_cost = max(max_cost, cost)

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for nei, cost in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        def can(score: int) -> bool:
            dist = [math.inf] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == math.inf:
                    continue

                if not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost < score:
                        continue

                    if not online[v]:
                        continue

                    new_cost = dist[u] + cost
                    if new_cost < dist[v] and new_cost <= k:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        # Binary search maximum possible minimum edge cost
        left, right = 0, max_cost
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans