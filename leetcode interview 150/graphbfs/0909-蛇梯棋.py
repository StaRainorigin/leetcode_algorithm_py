from typing import List
from collections import deque

# 08, 09, 10, 11
# 07, 06, 05, 04
# 00, 01, 02, 03

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if not board: return 0
        n, m = len(board), len(board[0])
        end = n * m 
        
        # 将位置转换为棋盘坐标
        def locate(pos: int):
            pos -= 1  # 转换为 0-based 索引
            i = pos // m  # 计算行
            j = pos % m if i % 2 == 0 else m - 1 - pos % m  # 计算列（考虑蛇形排列）
            return n - 1 - i, j  # 转换为棋盘坐标
        
        visited = {1}
        q = deque([1])
        count = 0
        
        while q:
            count += 1
            nxt = []
            while q:
                cur = q.popleft()
                for step in range(1, 7):
                    i, j = locate(cur + step)
                    next_pos = cur + step if board[i][j] == -1 else board[i][j]
                    if next_pos == end:
                        return count
                    if next_pos not in visited:
                        visited.add(next_pos)
                        nxt.append(next_pos)
            q.extend(nxt)
            
        return -1
            
if __name__ == "__main__":
    # board = [[-1,-1],[-1,1]]
    # board = [[-1,-1,-1,-1,-1,-1],
    #          [-1,-1,-1,-1,-1,-1],
    #          [-1,-1,-1,-1,-1,-1],
    #          [-1,35,-1,-1,13,-1],
    #          [-1,-1,-1,-1,-1,-1],
    #          [-1,15,-1,-1,-1,-1]]
    board = [[ 1, 1,-1],
             [ 1, 1, 1],
             [-1, 1, 1]]
    res = Solution().snakesAndLadders(board)
    print(res)