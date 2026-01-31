class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(len(prefix)):
            for s in strs[1:]:
                if i >= len(s) or s[i] != prefix[i]:
                    return prefix[:i]

        return prefix


if __name__ == "__main__":
    strs = input("Nhập các chuỗi (cách nhau bởi dấu phẩy): ").split(",")
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print("Longest Common Prefix:", result)
