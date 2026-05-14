class Solution:
    def combine(self, n, k):
        result = []

        def backtrack(start, path):

            # nếu đủ k số
            if len(path) == k:
                result.append(path[:])
                return

            # thử các số từ start -> n
            for num in range(start, n + 1):

                # chọn số
                path.append(num)

                # đệ quy
                backtrack(num + 1, path)

                # quay lui
                path.pop()

        backtrack(1, [])

        return result


if __name__ == "__main__":

    n = 4
    k = 2

    sol = Solution()

    result = sol.combine(n, k)

    print("Tất cả tổ hợp:")

    for combo in result:
        print(combo)