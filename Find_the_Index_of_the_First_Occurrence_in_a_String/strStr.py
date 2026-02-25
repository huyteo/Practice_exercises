class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    haystack = "sadbutsad"
    needle = "sad"

    result = solution.strStr(haystack, needle)
    print("Result:", result)