from typing import List, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return
        n, m = len(grid), len(grid[0])
        count = 0
        
        def dfs(i: int, j: int):
            nonlocal n, m
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
                    
        return count
    
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid: return
    #     n, m = len(grid), len(grid[0])
    #     visits: List[List[bool]] = [[False for _ in range(m)] for _ in range(n)]
    #     count = 0
        
    #     def dfs(i: int, j: int):
    #         nonlocal grid, visits, n, m
    #         visits[i][j] = True
    #         if (i+1 < n) and (not visits[i+1][j]) and (grid[i+1][j] == "1"):
    #             dfs(i+1, j)
    #         if (j+1 < m) and (not visits[i][j+1]) and (grid[i][j+1] == "1"):
    #             dfs(i, j+1)
    #         if (i-1 >= 0) and (not visits[i-1][j]) and (grid[i-1][j] == "1"):
    #             dfs(i-1, j)
    #         if (j-1 >= 0) and (not visits[i][j-1]) and (grid[i][j-1] == "1"):
    #             dfs(i, j-1)
        
    #     for i in range(n):
    #         for j in range(m):
    #             if grid[i][j] == "1" and not visits[i][j]:
    #                 count += 1
    #                 dfs(i, j)
            
    #     return count
    
 
    
if __name__ == "__main__":
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    solution = Solution()
    print(solution.numIslands(grid))