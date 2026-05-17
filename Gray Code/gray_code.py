class Solution:

    def grayCode(self, n):

        result = []

        for i in range(1 << n):

            gray = i ^ (i >> 1)

            result.append(gray)

        return result


if __name__ == "__main__":

    n = 2

    sol = Solution()

    result = sol.grayCode(n)

    print("Gray Code Sequence:")
    print(result)