class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  

        return closest_sum


if __name__ == "__main__":
    sol = Solution()

    nums = [-1, 2, 1, -4]
    target = 1
    print("Input:", nums, "Target:", target)
    print("Output:", sol.threeSumClosest(nums, target))

    nums = [0, 0, 0]
    target = 1
    print("\nInput:", nums, "Target:", target)
    print("Output:", sol.threeSumClosest(nums, target))
