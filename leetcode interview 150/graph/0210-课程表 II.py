from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
        
        status = [0] * numCourses
        ans = []
        
        def dfs(x: int) -> bool:
            if status[x] == 1:
                return True
            
            if status[x] == 2:
                return False
            
            status[x] = 1
            
            for y in graph[x]:
                if dfs(y):
                    return True
            status[x] = 2
            ans.append(x) # 只有不为环的路径才会加入, 因为递归所以是逆序加入的
            return False
        
        for i in range(numCourses):
            if status[i] == 0 and dfs(i):
                return []
            
        return ans[::-1]
            