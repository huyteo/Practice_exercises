class Solution:
    def uniquePaths(self, m, n):
        # Tạo mảng 1 chiều
        dp = [1] * n

        # Duyệt từng hàng
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[-1]


def main():
    print("=== UNIQUE PATHS ===")

    # Nhập dữ liệu
    m = int(input("Nhập số hàng (m): "))
    n = int(input("Nhập số cột (n): "))

    sol = Solution()
    result = sol.uniquePaths(m, n)

    print("👉 Số đường đi là:", result)


if __name__ == "__main__":
    main()