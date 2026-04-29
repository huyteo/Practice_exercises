class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        # DP 1D tối ưu bộ nhớ
        dp = [0] * n
        dp[0] = grid[0][0]

        # Hàng đầu tiên
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        # Các hàng còn lại
        for i in range(1, m):
            dp[0] += grid[i][0]  # cột đầu

            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]


def input_grid():
    m = int(input("Nhập số hàng (m): "))
    n = int(input("Nhập số cột (n): "))

    print("Nhập grid (các số cách nhau bằng dấu cách):")

    grid = []
    for i in range(m):
        while True:
            row = list(map(int, input(f"Hàng {i+1}: ").split()))
            if len(row) != n:
                print(f"⚠️ Bạn phải nhập đúng {n} số!")
            else:
                grid.append(row)
                break

    return grid


def print_grid(grid):
    print("\nGrid bạn đã nhập:")
    for row in grid:
        print(row)


def main():
    print("=== MINIMUM PATH SUM ===")

    grid = input_grid()
    print_grid(grid)

    sol = Solution()
    result = sol.minPathSum(grid)

    print("\n👉 Tổng nhỏ nhất là:", result)


if __name__ == "__main__":
    main()