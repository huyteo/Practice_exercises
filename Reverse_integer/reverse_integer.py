class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Kiểm tra tràn số
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return sign * rev
if __name__ == "__main__":
    sol = Solution()

    tests = [123, -123, 120, 0, 1534236469]

    for t in tests:
        print(f"x = {t} → reversed = {sol.reverse(t)}")
