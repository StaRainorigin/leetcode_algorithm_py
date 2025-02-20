class Solution:
    
    # 1: [1]; 2: [11, 2]; 3:[111, 12, 21]; 4[1111, 22, 121, 211, 112]
    
    def climbStairs(self, n: int) -> int:
        if n in range(3):
            return n
        n1, n2 = 1, 2
        for i in range(2, n):
            n1, n2 = n2, n1
            n2 += n1
        return n2
    
if __name__ == "__main__":
    print(Solution().climbStairs(3))