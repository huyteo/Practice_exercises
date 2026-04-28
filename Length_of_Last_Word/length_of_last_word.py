class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


if __name__ == "__main__":
    s = input("Nhập chuỗi: ")

    sol = Solution()
    result = sol.lengthOfLastWord(s)

    print("Độ dài từ cuối:", result)