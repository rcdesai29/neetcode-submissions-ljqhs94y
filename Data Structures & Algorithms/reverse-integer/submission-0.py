class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1
        sign = -1 if x <0 else 1

        res = 0
        
        x = abs(x)
        while x != 0:
            digit = x % 10
            x = int(x // 10)

            num = res * 10 + digit
            if num > MAX:
                return 0
            res = num
        return res * sign if MIN <= sign * res else 0
            