class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


def main():
    sol = Solution()

    test_cases = [1, 2, 3, 4, 5, 10]

    for n in test_cases:
        print(f"n = {n} -> {sol.climbStairs(n)} cách")


if __name__ == "__main__":
    main()