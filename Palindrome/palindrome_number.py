class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Trường hợp chắc chắn không phải palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    sol = Solution()

    tests = [121, -121, 10, 0, 1221, 12321]

    for t in tests:
        print(f"Input: {t} → Output:", sol.isPalindrome(t))
