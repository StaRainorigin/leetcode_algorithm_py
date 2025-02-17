class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        cols = [True] * n # 遍历到每行的状态. 由于防止直接禁用一列, 则某一列禁用之后, 下一行也一样禁用
        space = {'\\': [True]*(2*n-1), '/': [True]*(2*n-1)} # 用两个列表表示斜向禁用. 用两个列表禁用方向分开, 防止交叉禁用位置, 导致重复, 回溯时误回溯(本来是False, 又赋值False, 回溯一次就变成True的情况)
                                                          # 原理: 2*n-1个是为了防止越界错误; python中负索引是倒着数; 
        def dfs(row: int):
            if row == n:
                nonlocal ans
                ans += 1
                return
            for col, can_place in enumerate(cols):
                if can_place and space['\\'][row + col] and space['/'][row - col]:
                    cols[col] = space['\\'][row + col] = space['/'][row - col] = False
                    dfs(row + 1)
                    cols[col] = space['\\'][row + col] = space['/'][row - col] = True
        
        dfs(0)
        return ans
    
if __name__ == "__main__":
    print(Solution().totalNQueens(4))