class Solution:
    def canJump(self, nums):
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True


if __name__ == "__main__":
    nums = list(map(int, input("Nhập mảng: ").split()))

    sol = Solution()
    result = sol.canJump(nums)

    print("Có thể tới cuối mảng không?", result)