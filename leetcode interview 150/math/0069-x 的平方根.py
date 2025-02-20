class Solution:
    
# 1, 1; 2, 4; 5, 25; 6, 36; 
# 顺序走的简化都用二分

    def mySqrt(self, x: int) -> int:
        left, right = 0, min(x+1, 46341)
        while left < right:
            mid = (left + right) // 2
            if mid*mid > x:
                right = mid
            else:
                left = mid + 1
        return right - 1
        
        
        
if __name__ == "__main__":
    # print(pow((pow(2, 31) - 1), 0.5))
    print(Solution().mySqrt(4))