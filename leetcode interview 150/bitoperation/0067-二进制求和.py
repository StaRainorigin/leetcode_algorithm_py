class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        i, j, carry = 0, 0, 0
        ans = ""
        while i < n or j < m or carry:
            result = carry
            if i < n:
                result += 1 if a[n-1-i] == "1" else 0
                i += 1
            if j < m:
                result += 1 if b[m-1-j] == "1" else 0
                j += 1
            carry = result // 2
            result = result % 2
            ans += str(result)
        return ans[::-1]
            