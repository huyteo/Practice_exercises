class Solution:
    def subsets(self, nums):

        result = []

        def backtrack(start, path):

            # thêm subset hiện tại
            result.append(path[:])

            # thử thêm các phần tử tiếp theo
            for i in range(start, len(nums)):

                # chọn
                path.append(nums[i])

                # đệ quy
                backtrack(i + 1, path)

                # quay lui
                path.pop()

        backtrack(0, [])

        return result


if __name__ == "__main__":

    nums = [1, 2, 3]

    sol = Solution()

    result = sol.subsets(nums)

    print("Tất cả subset:")

    for subset in result:
        print(subset)