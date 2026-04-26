class Solution:
    def solveSudoku(self, board):

        def isValid(r, c, num):
            for i in range(9):
                if board[r][i] == num or board[i][c] == num:
                    return False

            startRow = (r // 3) * 3
            startCol = (c // 3) * 3

            for i in range(3):
                for j in range(3):
                    if board[startRow+i][startCol+j] == num:
                        return False

            return True


        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in "123456789":
                            if isValid(r, c, num):
                                board[r][c] = num
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True


        backtrack()


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    sol = Solution()
    sol.solveSudoku(board)

    for row in board:
        print(row)