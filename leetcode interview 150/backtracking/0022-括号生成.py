from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left_count = 0
        right_count = 0
        
        record = []
        ans = []
        
        def backtracking():
            nonlocal left_count, right_count
            if right_count == n:
                ans.append(''.join(record))
            
            
            if left_count < n:
                left_count += 1
                record.append('(')
                backtracking()
                record.pop()
                left_count -= 1
                
            if right_count < left_count:
                right_count += 1
                record.append(')')
                backtracking()
                record.pop()
                right_count -= 1
        
        backtracking()
        return ans

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))