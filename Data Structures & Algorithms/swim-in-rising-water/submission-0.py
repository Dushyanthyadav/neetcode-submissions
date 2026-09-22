class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            time, r, c = heapq.heappop(pq)
            
            if r == n - 1 and c == n - 1:
                return time
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(pq, (max(time, grid[nr][nc]), nr, nc))
                    
        return 0