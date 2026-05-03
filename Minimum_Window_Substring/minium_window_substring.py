from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # nếu ký tự đủ số lượng yêu cầu
            if char in need and window[char] == need[char]:
                have += 1

            # khi đã đủ tất cả ký tự
            while have == need_count:
                # cập nhật kết quả
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # thu nhỏ cửa sổ
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"

    sol = Solution()
    print("Kết quả:", sol.minWindow(s, t))