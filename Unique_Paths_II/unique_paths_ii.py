class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid), len(grid[0])

        # dp 1D tối ưu
        dp = [0] * n

        # ô bắt đầu
        dp[0] = 1 if grid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j] = 0  # gặp obstacle → không có đường
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]


def main():
    print("=== UNIQUE PATHS WITH OBSTACLES ===")

    # Nhập kích thước
    m = int(input("Nhập số hàng (m): "))
    n = int(input("Nhập số cột (n): "))

    print("Nhập grid (0 = đường đi, 1 = obstacle):")

    grid = []
    for i in range(m):
        row = list(map(int, input(f"Hàng {i+1}: ").split()))
        grid.append(row)

    sol = Solution()
    result = sol.uniquePathsWithObstacles(grid)

    print("👉 Số đường đi hợp lệ là:", result)


if __name__ == "__main__":
    main()