from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return None
        
        n, m = len(matrix), len(matrix[0])
        def get_num(index: int):
            return matrix[index//m][index%m]
        
        left, right = 0, n * m
        while left < right:
            mid = (left + right) // 2
            cur = get_num(mid)
            if cur < target:
                left = mid + 1
            elif cur > target:
                right = mid
            else:
                return True
        
        return False