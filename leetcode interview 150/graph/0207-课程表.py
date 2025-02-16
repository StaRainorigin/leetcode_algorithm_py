from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
            
        status = [0] * numCourses
        
        def dfs(x: int) -> bool:
            if status[x] == 1:
                return True # 正在访问时遇到正在访问的, 成环了
            elif status[x] == 2:
                return False
            
            status[x] = 1
            for y in graph[x]:
                if dfs(y):
                    return True
            status[x] = 2
            return False
        
        for i in range(numCourses):
            if status[i] == 0 and dfs(i):
                return False # dfs返回 True 说明有环, 返回 False(不行)
        
        return True
            
        
if __name__ == "__main__":
    pass