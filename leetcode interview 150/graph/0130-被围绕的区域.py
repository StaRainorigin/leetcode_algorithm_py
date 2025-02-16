from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        
        n, m = len(board), len(board[0])
        
        def dfs(i: int, j: int):
            nonlocal board
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
    # def solve(self, board: List[List[str]]) -> None:
    #     if not board: return
    #     n, m = len(board), len(board[0])
    #     visits: List[List[bool]] = [[False for _ in range(m)] for _ in range(n)]
    #     is_surrounded = True
        
    #     def dfs (i: int, j: int, change: bool):
    #         nonlocal board, n, m, visits, is_surrounded
    #         if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O' or (visits[i][j] and not change):
    #             return
    #         visits[i][j] = True
    #         if change:
    #             board[i][j] = 'X'
    #         elif i == 0 or i == n-1 or j == 0 or j == m-1:
    #             is_surrounded = False
    #         dfs(i+1, j, change)
    #         dfs(i, j+1, change)
    #         dfs(i, j-1, change)
    #         dfs(i-1, j, change)
            
    #     for i in range(n):
    #         for j in range(m):
    #             if board[i][j] == 'O' and not visits[i][j]:
    #                 is_surrounded = True
    #                 dfs(i, j, False)
    #                 if is_surrounded: dfs(i, j, True)

    #     return

if __name__ == "__main__":
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    board = [["O","O"],["O","O"]]
    
    s = Solution()
    s.solve(board)
    