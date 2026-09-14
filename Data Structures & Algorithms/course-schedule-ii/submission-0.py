from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return order if len(order) == numCourses else []
        