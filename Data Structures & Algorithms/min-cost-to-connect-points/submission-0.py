class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = [False] * n
        total_cost = 0
        
        for _ in range(n):
            curr = -1
            curr_dist = float('inf')
            
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_dist:
                    curr_dist = min_dist[i]
                    curr = i
            
            visited[curr] = True
            total_cost += curr_dist
            
            for next_node in range(n):
                if not visited[next_node]:
                    dist = abs(points[curr][0] - points[next_node][0]) + abs(points[curr][1] - points[next_node][1])
                    if dist < min_dist[next_node]:
                        min_dist[next_node] = dist
                        
        return total_cost
        