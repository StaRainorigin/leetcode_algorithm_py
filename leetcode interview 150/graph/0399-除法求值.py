from collections import defaultdict
from typing import List


class Solution:
    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), w in zip(equations, values):
            graph[u].append((v, w))
            graph[v].append((u, 1/w))
        
        def bfs(start: int, end: int, visited):
            pass
    
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), w in zip(equations, values):
            graph[u].append((v, w))
            graph[v].append((u, 1/w))
            
        def dfs(start: int, end: int, visited: set):
            if start not in graph or end not in graph: return -1.0
            if start == end: return 1.0
            
            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            
            return -1.0
        
        result = []
        for u, v in queries:
            visited = set()
            result.append(dfs(u, v, visited))
        
        return result