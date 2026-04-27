class Solution:
    def myPow(self, x, n):
        def fastPow(x, n):
            if n == 0:
                return 1
            
            half = fastPow(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        if n < 0:
            x = 1 / x
            n = -n

        return fastPow(x, n)


if __name__ == "__main__":
    x = 2.0
    n = 10

    sol = Solution()
    print(sol.myPow(x, n))