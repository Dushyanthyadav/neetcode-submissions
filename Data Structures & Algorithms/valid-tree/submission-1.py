class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        return len(visited) == n