class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        direction = -1  

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            current_row += direction

        return "".join(rows)


if __name__ == "__main__":
    solution = Solution()

    s = "PAYPALISHIRING"
    numRows = 3

    result = solution.convert(s, numRows)
    print("Input:", s)
    print("Rows:", numRows)
    print("Output:", result)
