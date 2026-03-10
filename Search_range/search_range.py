class Solution:
    def searchRange(self, nums, target):

        def findFirst(nums, target):
            left = 0
            right = len(nums) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first


        def findLast(nums, target):
            left = 0
            right = len(nums) - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last

        return [findFirst(nums, target), findLast(nums, target)]



if __name__ == "__main__":

    nums = [1,3,3,5,6,7,8]
    target = 3

    solution = Solution()

    result = solution.searchRange(nums, target)

    print("Array:", nums)
    print("Target:", target)
    print("First and Last Position:", result)