class Solution:

    def subsetsWithDup(self, nums):

        nums.sort()

        result = []

        def backtrack(start, path):

            result.append(path[:])

            for i in range(start, len(nums)):

                # Tránh duplicate
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])

        return result


if __name__ == "__main__":

    nums = [1, 2, 2]

    sol = Solution()

    result = sol.subsetsWithDup(nums)

    print("All unique subsets:")

    for subset in result:
        print(subset)