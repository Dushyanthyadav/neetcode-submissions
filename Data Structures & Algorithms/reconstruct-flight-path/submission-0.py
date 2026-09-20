from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        route = []
        
        def dfs(airport: str) -> None:
            while graph[airport]:
                dfs(graph[airport].pop())
            route.append(airport)
            
        dfs("JFK")
        return route[::-1]