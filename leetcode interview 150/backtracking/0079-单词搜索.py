from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        n, m = len(board), len(board[0])
        visited = set()
        
        def dfs(i: int, j: int, index: int):
            if index == len(word):
                return True
            
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or word[index] != board[i][j]:
                return False
            
            visited.add((i, j))
            for u, v in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if dfs(u, v, index+1):
                    return True
            visited.remove((i, j))
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        
        return False