class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                        visited.add(nei)
                        dfs(nei)
            return

        connected = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                connected += 1
        return connected