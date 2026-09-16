class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) 
            return parent[i]
            
        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1
                
        return components