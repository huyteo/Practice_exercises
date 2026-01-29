class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if result > 214748364 or (
                result == 214748364 and digit > 7
            ):
                return 2147483647 if sign == 1 else -2147483648

            result = result * 10 + digit
            i += 1

        return sign * result


if __name__ == "__main__":
    sol = Solution()

    tests = [
        "42",
        "   -042",
        "1337c0d3",
        "0-1",
        "words and 987"
    ]

    for t in tests:
        print(f'Input: "{t}" → Output:', sol.myAtoi(t))
