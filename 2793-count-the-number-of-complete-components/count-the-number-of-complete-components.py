class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build graph
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        ans = 0

        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, component)

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)

                # A complete graph with k vertices has k*(k-1)/2 edges
                vertices = len(component)
                edge_count = sum(len(graph[node]) for node in component) // 2

                if edge_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans