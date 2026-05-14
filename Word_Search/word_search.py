class Solution:
    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            # tìm đủ word
            if index == len(word):
                return True

            # sai điều kiện
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[index]):
                return False

            # lưu ký tự hiện tại
            temp = board[r][c]

            # đánh dấu đã dùng
            board[r][c] = "#"

            # DFS 4 hướng
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # backtracking
            board[r][c] = temp

            return found

        # thử từ mọi ô
        for r in range(rows):
            for c in range(cols):

                if dfs(r, c, 0):
                    return True

        return False


if __name__ == "__main__":

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]

    word = "ABCCED"

    sol = Solution()

    result = sol.exist(board, word)

    print("Kết quả:", result)