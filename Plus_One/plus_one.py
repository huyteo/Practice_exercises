class Solution:
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


def main():
    sol = Solution()

    test_cases = [
        [1,2,3],
        [4,3,2,1],
        [9],
        [9,9,9],
        [1,9,9]
    ]

    for digits in test_cases:
        print(f"{digits} -> {sol.plusOne(digits[:])}")


if __name__ == "__main__":
    main()