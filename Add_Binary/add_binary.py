class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])


def main():
    sol = Solution()

    test_cases = [
        ("11", "1"),
        ("1010", "1011"),
        ("0", "0"),
        ("111", "1")
    ]

    for a, b in test_cases:
        print(f"{a} + {b} = {sol.addBinary(a, b)}")


if __name__ == "__main__":
    main()