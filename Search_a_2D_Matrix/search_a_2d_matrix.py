class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


def main():
    matrix = [
        [1, 3, 5, 7],
        [10,11,16,20],
        [23,30,34,60]
    ]

    sol = Solution()

    targets = [3, 13, 60, 1]

    for t in targets:
        print(f"target = {t} → {sol.searchMatrix(matrix, t)}")


if __name__ == "__main__":
    main()