class Solution:

    def largestRectangleArea(self, heights):

        stack = []
        max_area = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width

                max_area = max(max_area, area)

            stack.append(i)

        heights.pop()

        return max_area


    def maximalRectangle(self, matrix):

        if not matrix:
            return 0

        cols = len(matrix[0])

        heights = [0] * cols

        max_area = 0

        for row in matrix:

            for i in range(cols):

                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            max_area = max(
                max_area,
                self.largestRectangleArea(heights)
            )

        return max_area


if __name__ == "__main__":

    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]

    sol = Solution()

    result = sol.maximalRectangle(matrix)

    print("Maximal Rectangle Area:", result)