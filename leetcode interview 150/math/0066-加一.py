from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = []
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            result = digits[i] + carry
            if result > 9:
                result %= 10
            else:
                carry = 0
            new_digits.append(result)
            i -= 1
        if carry: 
            new_digits.append(carry)
        return new_digits[::-1]
            