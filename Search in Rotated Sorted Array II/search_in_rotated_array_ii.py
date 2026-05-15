class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # nếu tìm thấy
            if nums[mid] == target:
                return True

            # trường hợp duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # bên trái sorted
            elif nums[left] <= nums[mid]:

                # target nằm trong bên trái
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # bên phải sorted
            else:

                # target nằm trong bên phải
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == "__main__":

    nums = [2,5,6,0,0,1,2]
    target = 0

    sol = Solution()

    result = sol.search(nums, target)

    print("Kết quả:", result)