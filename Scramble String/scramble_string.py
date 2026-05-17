from functools import lru_cache


class Solution:

    def isScramble(self, s1, s2):

        @lru_cache(None)
        def dfs(a, b):

            if a == b:
                return True

            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for i in range(1, n):

                # Không swap
                if (dfs(a[:i], b[:i]) and
                    dfs(a[i:], b[i:])):
                    return True

                # Swap
                if (dfs(a[:i], b[n-i:]) and
                    dfs(a[i:], b[:n-i])):
                    return True

            return False

        return dfs(s1, s2)


if __name__ == "__main__":

    s1 = "great"
    s2 = "rgeat"

    sol = Solution()

    result = sol.isScramble(s1, s2)

    print("Is Scramble:", result)