class Solution:
    def isPalindrome(self, x: int) -> bool:
        a, y = x, 0
        while a > 0:
            y = y * 10 + (a % 10)
            a = a // 10
        return x == y