class Solution:
    def totalNQueens(self, n):
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        count = 0

        def backtrack(row):
            nonlocal count

            # Nếu đã đặt đủ n quân hậu
            if row == n:
                count += 1
                return

            for col in range(n):
                # Kiểm tra hợp lệ
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Đặt hậu
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Sang hàng tiếp theo
                backtrack(row + 1)

                # Quay lui (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return count


# ================== MAIN ==================
if __name__ == "__main__":
    n = int(input("Nhập n: "))

    sol = Solution()
    result = sol.totalNQueens(n)

    print("Số cách đặt", n, "quân hậu là:", result)