class Solution:
    def searchInsert(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left


if __name__ == "__main__":

    nums = [1,3,5,6]
    target = 2

    solution = Solution()

    result = solution.searchInsert(nums, target)

    print("Array:", nums)
    print("Target:", target)
    print("Insert Position:", result)