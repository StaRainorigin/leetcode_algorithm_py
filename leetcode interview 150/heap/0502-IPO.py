from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if not capital or capital[0] > w:
            return w
        max_heap = []
        i, n = 0, len(profits)
        while k > 0:
            
            while i < n and capital[i] <= w:
                heappush(max_heap, -profits[i])
                i += 1
                
            if not max_heap:
                break
            
            w -= heappop(max_heap)
            k -= 1
            
        return w
    

if __name__ == "__main__":
    # k, w, profits, capital = 2, 0, [1, 2, 3], [0, 1, 1]
    # print(Solution().findMaximizedCapital(k, w, profits, capital))
    print(Solution().findMaximizedCapital(10, 0, [1, 2, 3], [0, 1, 2]))