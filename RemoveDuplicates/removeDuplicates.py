class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


# ===== TEST CODE =====
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]

    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("k =", k)
    print("Unique elements:", nums[:k])
    print("Full array:", nums)